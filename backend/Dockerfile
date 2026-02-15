# ==========================================================
# DO NOT MODIFY DEPLOYMENT MODEL WITHOUT APPROVAL
# This container runs on Google Cloud Run.
# Cloud Run containers are stateless.
# No persistent filesystem storage allowed.
# Do NOT introduce local databases or background services.
# ==========================================================

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required by some Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the embedding model into the image at build time.
# This avoids downloading it on every Cloud Run cold start.
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
