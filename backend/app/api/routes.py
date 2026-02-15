from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

from ..rag.retriever import retrieve_context
from ..rag.generator import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat_endpoint(request: Request, payload: ChatRequest):
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    collection = request.app.state.collection

    context_chunks, confidence, sources = retrieve_context(collection, payload.question)

    answer = generate_answer(payload.question, context_chunks)

    return {
        "answer": answer,
        "confidence": round(confidence, 3),
        "sources": sources
    }