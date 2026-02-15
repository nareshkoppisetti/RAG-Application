import re
from pathlib import Path
from typing import List

# These filename suffixes are redundant variants of primary files.
# Skipping them reduces chunk count from 405 → ~122, well within free tier limits.
REDUNDANT_SUFFIXES = [
    "_respond",
    "_add-azure-ad-app",
    "_cleanup-previous-sso",
    "_copy-app-metadata",
    "_deploy-ebs-accessgate",
    "_ebs-accessgate-patches",
    "_ebs-sso-registration",
    "_quote",
    "_trial",
    "_benefits",
    "_saml",
]


def is_redundant_file(file_path: Path) -> bool:
    """Returns True if this file is a redundant variant that should be skipped."""
    stem = file_path.stem
    if "%20" in file_path.name:
        return True
    return any(stem.endswith(suffix) for suffix in REDUNDANT_SUFFIXES)


def remove_frontmatter(text: str) -> str:
    return re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL)


def remove_html_tags(text: str) -> str:
    text = re.sub(r"<(script|style).*?>.*?</\1>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    return text


def normalize_whitespace(text: str) -> str:
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def clean_markdown(text: str) -> str:
    text = remove_frontmatter(text)
    text = remove_html_tags(text)
    text = normalize_whitespace(text)
    return text


def chunk_text(text: str, chunk_size: int = 3000, overlap: int = 200) -> List[str]:
    chunks = []
    start = 0
    length = len(text)

    while start < length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks


def load_and_chunk_data(data_path: Path) -> List[dict]:
    documents = []

    for file_path in data_path.rglob("*.md"):
        if is_redundant_file(file_path):
            continue

        raw_text = file_path.read_text(encoding="utf-8")
        cleaned_text = clean_markdown(raw_text)
        chunks = chunk_text(cleaned_text)

        for chunk in chunks:
            documents.append({
                "content": chunk,
                "source": file_path.name
            })

    return documents