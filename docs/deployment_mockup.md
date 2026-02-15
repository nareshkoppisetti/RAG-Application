# Deployment Architecture

User
  ↓
Vercel (Frontend)
  ↓
Cloud Run (FastAPI Docker)
  ↓
Chroma (In-Memory)
  ↓
Gemini API

## Cloud Run Settings

- Min instances: 1
- Max instances: 1
- Stateless container
- No disk persistence
