from .embedder import load_model, embedded_query, embedded_texts
from .similarity import rank_by_similarity


def build_index(chunks: list[dict], model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> dict:
    model = load_model(model_name)
    texts = [c["text"] for c in chunks]
    embeddings = embedded_texts(model, texts)

    return {
        "model_name": model_name,
        "model": model,
        "chunks": chunks,
        "embeddings": embeddings,
    }


def search(index: dict, query: str, k: int = 1) -> list[dict]:
    model = index["model"]
    chunks = index["chunks"]
    embeddings = index["embeddings"]

    q = embedded_query(model, query)
    ranked_chunks = rank_by_similarity(q, embeddings)[:k]

    results = []
    for idx, score in ranked_chunks:
        c = chunks[idx]
        results.append({
            "score": score,
            "text": c["text"],
            "source": c.get("source"),
            "chunk_index": c.get("chunk_index") or c.get("id"),
            "metadata": c.get("metadata", {})
        })
    return results