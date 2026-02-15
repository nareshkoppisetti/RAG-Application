from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.routes import router as chat_router
from .api.health import router as health_router
from .rag.startup_index import build_vector_store

app = FastAPI(title="Organization RAG API")

# CORS — allows frontend to call the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://rag-application-chat.vercel.app/",  # your Vercel URL
        "https://*.vercel.app",  # allows all Vercel preview URLs
    ],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    collection = build_vector_store()
    app.state.collection = collection

app.include_router(chat_router)
app.include_router(health_router)