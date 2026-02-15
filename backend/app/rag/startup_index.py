"""
==========================================================
VECTOR STORE INITIALIZATION

This application runs on Google Cloud Run.
Containers are stateless and filesystem is ephemeral.

Chroma MUST:
- Be built in memory
- Not persist to disk
- Not create local database files

DO NOT introduce file-based persistence here.
==========================================================
"""

from pathlib import Path
import time
import chromadb

from .chunking import load_and_chunk_data
from .embeddings import embed_batch


DATA_PATH = Path("data")
BATCH_SIZE = 90  # Stay safely under the 100 requests/min free tier limit


def build_vector_store():
    """
    Builds Chroma vector store in memory.
    """

    print("Loading and chunking markdown files...")
    documents = load_and_chunk_data(DATA_PATH)
    print(f"Total chunks created: {len(documents)}")

    client = chromadb.Client()
    collection = client.create_collection(name="org_rag_collection")

    print("Generating embeddings and inserting into Chroma...")

    total = len(documents)
    for start in range(0, total, BATCH_SIZE):
        batch = documents[start: start + BATCH_SIZE]
        texts = [doc["content"] for doc in batch]

        embeddings = embed_batch(texts)

        collection.add(
            ids=[str(start + i) for i in range(len(batch))],
            embeddings=embeddings,
            documents=texts,
            metadatas=[{"source": doc["source"]} for doc in batch]
        )

        print(f"  Indexed {min(start + BATCH_SIZE, total)}/{total} chunks...")

        # Only wait between batches, not after the last one
        if start + BATCH_SIZE < total:
            time.sleep(62)  # Wait 62s between batches to reset the per-minute quota

    print("Vector store successfully built.")
    return collection