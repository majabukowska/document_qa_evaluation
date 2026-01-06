from pathlib import Path

from src.ingestion.loader import load_document
from src.ingestion.cleaner import clean_text
from src.ingestion.chunker import chunk_text


if __name__ == "__main__":
    path = Path("data/raw/What is PyTorch_ _ IBM.html")

    raw_text = load_document(path)
    print("===== RAW (first 500 chars) =====")
    print(raw_text[:500])

    cleaned_text = clean_text(raw_text)
    print("\n===== CLEANED (first 500 chars) =====")
    print(cleaned_text[:500])

    chunks = chunk_text(
        cleaned_text,
        source=path.name,
        max_words=400,
        overlap=50,
    )

    print(f"\n===== CHUNKS COUNT: {len(chunks)} =====\n")

    for chunk in chunks[:3]:
        words = len(chunk["text"].split())
        print(f"--- CHUNK {chunk['id']} ({words} words) ---")
        print(chunk["text"][:600])
        print()
