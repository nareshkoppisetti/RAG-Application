from typing import List, Tuple
from .embeddings import embed_query

TOP_K = 10


def retrieve_context(collection, query: str) -> Tuple[List[str], float, List[str]]:
    """
    Retrieve relevant context chunks with accuracy scoring
    """
    
    print(f"\n{'='*70}")
    print(f"🔍 RETRIEVAL for: '{query}'")
    print(f"{'='*70}")
    
    try:
        # Generate embedding for the query
        query_embedding = embed_query(query)
        print(f"✅ Query embedded successfully")

        # Search in vector database
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=TOP_K
        )

        documents = results.get("documents", [[]])[0]
        distances = results.get("distances", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        if not documents:
            print(f"❌ No documents found!")
            print(f"📊 ACCURACY SCORE: 0.0% (No matches)")
            print(f"{'='*70}\n")
            return [], 0.0, []

        # Calculate similarity scores (lower distance = higher similarity)
        similarities = [1 - d for d in distances]
        
        print(f"\n📊 Found {len(documents)} relevant chunks:")
        print(f"{'─'*70}")
        
        # Show top 5 matches with scores
        for i, (doc, sim, meta) in enumerate(zip(documents[:5], similarities[:5], metadatas[:5]), 1):
            source = meta.get("source", "unknown")
            preview = doc[:100].replace('\n', ' ').replace('\r', ' ')
            
            # Color code the score
            if sim > 0.7:
                quality = "🟢 EXCELLENT"
            elif sim > 0.5:
                quality = "🟡 GOOD"
            elif sim > 0.3:
                quality = "🟠 FAIR"
            else:
                quality = "🔴 POOR"
            
            print(f"{i}. {quality} | Score: {sim:.3f} ({sim*100:.1f}%)")
            print(f"   Source: {source}")
            print(f"   Preview: {preview}...")
            print(f"{'─'*70}")
        
        # Get unique sources
        sources = [meta.get("source", "") for meta in metadatas]
        unique_sources = list(dict.fromkeys(sources))
        max_similarity = max(similarities) if similarities else 0.0
        avg_similarity = sum(similarities[:5]) / min(5, len(similarities)) if similarities else 0.0
        
        # Calculate overall accuracy score
        accuracy_score = (max_similarity * 0.6 + avg_similarity * 0.4) * 100
        
        # Determine accuracy grade
        if accuracy_score >= 70:
            grade = "🟢 HIGH"
        elif accuracy_score >= 50:
            grade = "🟡 MEDIUM"
        elif accuracy_score >= 30:
            grade = "🟠 LOW"
        else:
            grade = "🔴 VERY LOW"
        
        print(f"\n📊 RETRIEVAL ACCURACY METRICS:")
        print(f"{'─'*70}")
        print(f"   Best Match Score:    {max_similarity:.3f} ({max_similarity*100:.1f}%)")
        print(f"   Avg Top-5 Score:     {avg_similarity:.3f} ({avg_similarity*100:.1f}%)")
        print(f"   Overall Accuracy:    {accuracy_score:.1f}% {grade}")
        print(f"   Relevant Sources:    {len(unique_sources)}")
        print(f"{'─'*70}")
        print(f"📁 Sources: {', '.join(unique_sources[:3])}")
        if len(unique_sources) > 3:
            print(f"   ... and {len(unique_sources) - 3} more")
        print(f"{'='*70}\n")

        return documents, max_similarity, unique_sources
        
    except Exception as e:
        print(f"❌ RETRIEVAL ERROR: {e}")
        print(f"📊 ACCURACY SCORE: 0.0% (Error)")
        print(f"{'='*70}\n")
        return [], 0.0, []