from pathlib import Path
from src.ingestion.loader import load_document
from src.ingestion.cleaner import clean_text
from src.ingestion.chunker import chunk_text

from src.retrieval.search import build_index, search

raw = load_document(Path("data/raw/What is PyTorch_ _ IBM.html"))
cleaned = clean_text(raw)
chunks = chunk_text(cleaned, source="IBM PyTorch", max_words=400, overlap=50)

idx = build_index(chunks)

results = search(idx, "What is PyTorch?", k=3)
for r in results:
    print("\n---")
    print(f"score={r['score']:.3f} source={r['source']} chunk={r['chunk_index']}")
    print(r["text"][:300])
