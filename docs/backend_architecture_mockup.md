# Backend Architecture

Frontend
   ↓
POST /chat
   ↓
routes.py
   ↓
RAG Service
   ↓
retriever.py
   ↓
generator.py
   ↓
Response

## Responsibilities

routes.py
- Validate input
- Call RAG logic

retriever.py
- Embed query
- Retrieve chunks
- Apply similarity threshold

generator.py
- Inject context
- Call Gemini API

startup_index.py
- Load markdown files
- Chunk
- Generate embeddings
- Build Chroma in memory
