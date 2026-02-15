from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # downloads once, runs locally forever


def embed_batch(texts: list[str]) -> list[list[float]]:
    return model.encode(texts, show_progress_bar=True).tolist()


def embed_text(text: str) -> list[float]:
    return model.encode(text).tolist()


def embed_query(text: str) -> list[float]:
    return embed_text(text)