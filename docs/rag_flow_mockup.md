# RAG Flow Design

User Question
   ↓
Generate Embedding
   ↓
Similarity Search (Top 5)
   ↓
Apply Similarity Threshold (>= 0.75)
   ↓
If below threshold → Fallback
   ↓
If above threshold → Send Context to Gemini
   ↓
Generate Grounded Answer
   ↓
Return Response
