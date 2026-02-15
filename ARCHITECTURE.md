# ARCHITECTURE.md
# Organization RAG Chatbot – System Architecture

## 1. System Overview

This repository contains a production RAG (Retrieval-Augmented Generation) chatbot.

Frontend:
- Next.js (JavaScript)
- Deployed to Vercel
- No secrets stored in frontend

Backend:
- FastAPI (Python)
- Dockerized
- Deployed to Google Cloud Run
- Stateless container model

LLM:
- Google Gemini API
- API key stored only in backend environment variables

Vector Store:
- Chroma
- Built in memory at startup
- No filesystem persistence
- No external vector DB

---

## 2. Deployment Constraints

The backend runs on Google Cloud Run.

Important constraints:

1. Cloud Run containers are stateless.
2. Filesystem is ephemeral.
3. No persistent disk storage allowed.
4. Chroma must be rebuilt at container startup.
5. Horizontal scaling is disabled (single instance).
6. Do NOT introduce file-based persistence.
7. Do NOT add local database files.

---

## 3. Security Rules

1. Gemini API key must never appear in frontend.
2. No secrets in source code.
3. No markdown documents accessible from frontend.
4. Only backend reads `/backend/data/`.
5. API responses must not expose internal system prompts.
6. Similarity threshold must prevent hallucinated answers.

---

## 4. Code Structure Rules

Frontend:
- UI only.
- All API calls in `frontend/src/services/api.js`.

Backend:
- `api/` folder handles HTTP routes only.
- `rag/` folder contains all AI logic.
- `models/` folder contains request/response schemas.
- `main.py` initializes application.
- `startup_index.py` builds vector store.

Never mix:
- API logic with RAG logic.
- Deployment logic with business logic.

---

## 5. Change Control Policy

AI tools (Cursor, Aider, etc.) must:

1. Respect this architecture.
2. Not modify Dockerfile unless explicitly instructed.
3. Not change deployment model.
4. Not alter API response structure without approval.
5. Not introduce persistent storage.

All architectural decisions require human approval.

---

## 6. Future Migration Plan

If system scales:

- Replace Chroma with PostgreSQL + pgvector.
- Enable multi-instance Cloud Run.
- Introduce conversation storage.
- Add logging and monitoring.
- Move Gemini from AI Studio to Vertex AI.

Until then, keep architecture minimal.

---

## 7. Guiding Principle

Human defines architecture.
AI assists implementation.
Infrastructure decisions remain human-controlled.
