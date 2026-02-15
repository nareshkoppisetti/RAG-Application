import os
import time
from google import genai
from dotenv import load_dotenv
from .prompts import SYSTEM_PROMPT

load_dotenv(override=True)

GEN_MODEL = "gemini-1.5-flash"

# Rate limiting
_request_times = []
MAX_REQUESTS_PER_MINUTE = 10

# Simple cache
_answer_cache = {}


def _wait_if_rate_limited():
    global _request_times
    current_time = time.time()
    _request_times = [t for t in _request_times if current_time - t < 60]
    
    if len(_request_times) >= MAX_REQUESTS_PER_MINUTE:
        wait_time = 65 - (current_time - min(_request_times))
        if wait_time > 0:
            print(f"⏳ Rate limit: waiting {wait_time:.0f}s...")
            time.sleep(wait_time)
            _request_times = []
    
    _request_times.append(current_time)


def _calculate_response_quality(answer: str, context_chunks: list, used_api: bool) -> dict:
    """
    Calculate quality metrics for the response
    """
    
    # Length check
    length_score = min(100, (len(answer) / 200) * 100) if answer else 0
    
    # Context usage check
    context_score = min(100, len(context_chunks) * 15) if context_chunks else 0
    
    # Source check (API responses are generally better)
    source_score = 80 if used_api else 60
    
    # Overall quality
    overall_quality = (length_score * 0.3 + context_score * 0.4 + source_score * 0.3)
    
    # Determine grade
    if overall_quality >= 75:
        grade = "🟢 EXCELLENT"
    elif overall_quality >= 60:
        grade = "🟡 GOOD"
    elif overall_quality >= 40:
        grade = "🟠 FAIR"
    else:
        grade = "🔴 POOR"
    
    return {
        'overall': overall_quality,
        'grade': grade,
        'length_score': length_score,
        'context_score': context_score,
        'source_score': source_score
    }


def _create_smart_answer(query: str, context_chunks: list, confidence: float) -> str:
    """
    Create answer based on context WITHOUT calling API
    """
    
    if not context_chunks:
        return """I couldn't find specific information about that in our documentation.

I can help with:
• SSO solutions and integrations
• Oracle EBS, PeopleSoft, JDE, SAP
• Azure AD, ADFS, Okta configurations

Please contact our support team for more details."""
    
    if confidence < 0.3:
        return f"""I found some related information in our documentation, but I'm not confident it fully answers your question.

Here's what I found:

{context_chunks[0][:400]}...

For accurate information about "{query}", please contact our support team."""
    
    # Common questions
    query_lower = query.lower()
    
    if 'what is sso' in query_lower or 'define sso' in query_lower:
        return """SSO stands for Single Sign-On. It's an authentication method that allows users to access multiple applications with one set of login credentials.

Based on our documentation:
• SSOGEN provides SSO solutions for enterprise applications
• We support Oracle EBS, PeopleSoft, JDE, and SAP
• Integration with Azure AD, ADFS, Okta, and other identity providers
• Simplifies user authentication and improves security

For detailed information about our SSO solutions, please contact our support team."""
    
    if 'what does ssogen do' in query_lower or 'about ssogen' in query_lower:
        return """SSOGEN Corporation is a software development company specializing in SSO (Single Sign-On) solutions.

Our Mission:
• Provide NextGen SSO Security Solutions
• Simplify SSO Integrations
• Make SSO Affordable

We help organizations:
• Implement web security
• Protect mission-critical applications
• Prevent unauthorized access to confidential data
• Provide seamless user experience

Supported Applications: Oracle EBS, PeopleSoft, JDE, SAP, and many more.

Contact us for demos, quotes, or technical questions."""
    
    return f"""Based on our documentation:

{context_chunks[0][:600]}

For more detailed information, please contact our support team at SSOGEN Corporation."""


def generate_answer(query: str, context_chunks: list) -> str:
    """
    Generate answer with quality scoring
    """
    
    print(f"\n{'='*70}")
    print(f"🤖 GENERATION for: '{query}'")
    print(f"{'='*70}")
    
    used_api = False
    answer_source = "FALLBACK"
    
    # Handle greetings
    greetings = ['hi', 'hello', 'hey', 'good morning', 'good afternoon', 'good evening']
    if query.lower().strip() in greetings:
        print("💬 Greeting detected")
        answer = """Hello! I'm your SSOGEN assistant. 

I can help you with:
• SSO (Single Sign-On) solutions
• Oracle EBS, PeopleSoft, JDE, SAP integrations
• Azure AD, ADFS, Okta, SAML configurations
• Our products and services

What would you like to know?"""
        answer_source = "CANNED_RESPONSE"
        
        # Print simple metrics for greetings
        print(f"\n📊 RESPONSE QUALITY: N/A (Greeting)")
        print(f"{'='*70}\n")
        return answer
    
    # Check cache
    cache_key = query.lower().strip()
    if cache_key in _answer_cache:
        print("✅ Using cached answer")
        answer = _answer_cache[cache_key]
        answer_source = "CACHE"
        
        # Calculate and print quality
        quality = _calculate_response_quality(answer, context_chunks, False)
        print(f"\n📊 RESPONSE QUALITY METRICS:")
        print(f"{'─'*70}")
        print(f"   Overall Quality:     {quality['overall']:.1f}% {quality['grade']}")
        print(f"   Answer Length:       {len(answer)} chars ({quality['length_score']:.1f}%)")
        print(f"   Context Usage:       {len(context_chunks)} chunks ({quality['context_score']:.1f}%)")
        print(f"   Source Quality:      {quality['source_score']:.1f}%")
        print(f"   Answer Source:       {answer_source}")
        print(f"{'─'*70}")
        print(f"{'='*70}\n")
        
        return answer
    
    # Calculate confidence
    confidence = 0.5
    if context_chunks and len(context_chunks) > 0:
        confidence = min(0.9, 0.3 + (len(context_chunks) * 0.1))
    
    print(f"📚 Context: {len(context_chunks)} chunks (confidence: {confidence:.2f})")
    
    # For low confidence, use smart answer
    if confidence < 0.4 or not context_chunks:
        print("⚠️ Low confidence - using smart fallback answer")
        answer = _create_smart_answer(query, context_chunks, confidence)
        answer_source = "SMART_FALLBACK"
        _answer_cache[cache_key] = answer
        
        # Calculate and print quality
        quality = _calculate_response_quality(answer, context_chunks, False)
        print(f"\n📊 RESPONSE QUALITY METRICS:")
        print(f"{'─'*70}")
        print(f"   Overall Quality:     {quality['overall']:.1f}% {quality['grade']}")
        print(f"   Answer Length:       {len(answer)} chars ({quality['length_score']:.1f}%)")
        print(f"   Context Usage:       {len(context_chunks)} chunks ({quality['context_score']:.1f}%)")
        print(f"   Source Quality:      {quality['source_score']:.1f}%")
        print(f"   Answer Source:       {answer_source}")
        print(f"{'─'*70}")
        print(f"{'='*70}\n")
        
        return answer
    
    # Try API
    top_chunks = context_chunks[:3]
    context = "\n\n".join(top_chunks)
    
    print(f"📏 Context length: {len(context)} chars")
    
    prompt = f"""Answer this question briefly based on the info below:

{context[:2000]}

Question: {query}

Brief answer:"""
    
    print(f"🔄 Trying Gemini API (30s timeout)...")
    
    try:
        _wait_if_rate_limited()
        
        client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY"),
            http_options={"timeout": 30}
        )
        
        response = client.models.generate_content(
            model=GEN_MODEL,
            contents=prompt,
            config={
                'temperature': 0.3,
                'max_output_tokens': 300,
            }
        )
        
        if response and hasattr(response, 'text') and response.text:
            answer = response.text.strip()
            used_api = True
            answer_source = "GEMINI_API"
            print(f"✅ API SUCCESS!")
            _answer_cache[cache_key] = answer
        else:
            raise Exception("Empty response")
    
    except Exception as e:
        error_type = type(e).__name__
        print(f"❌ API failed: {error_type}")
        print(f"⚡ Using smart fallback answer instead")
        answer = _create_smart_answer(query, context_chunks, confidence)
        answer_source = "API_FALLBACK"
        _answer_cache[cache_key] = answer
    
    # Calculate and print quality metrics
    quality = _calculate_response_quality(answer, context_chunks, used_api)
    
    print(f"\n📊 RESPONSE QUALITY METRICS:")
    print(f"{'─'*70}")
    print(f"   Overall Quality:     {quality['overall']:.1f}% {quality['grade']}")
    print(f"   Answer Length:       {len(answer)} chars ({quality['length_score']:.1f}%)")
    print(f"   Context Usage:       {len(context_chunks)} chunks ({quality['context_score']:.1f}%)")
    print(f"   Source Quality:      {quality['source_score']:.1f}%")
    print(f"   Answer Source:       {answer_source}")
    print(f"   API Used:            {'✅ Yes' if used_api else '❌ No (Fallback)'}")
    print(f"{'─'*70}")
    print(f"{'='*70}\n")
    
    return answer