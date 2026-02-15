# Error Handling Strategy

1. Gemini API Failure
Return:
"Service temporarily unavailable."

2. No Retrieval Match
Return fallback message.

3. Invalid Input
Return 400 Bad Request.

4. Rate Limit Exceeded
Return 429 Too Many Requests.
