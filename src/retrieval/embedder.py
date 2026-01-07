import numpy as np
from sentence_transformers import SentenceTransformer


def load_model(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    return SentenceTransformer(model_name)


def embedded_texts(model, texts: list[str]) -> np.ndarray:
    return model.encode(texts, show_progress_bar=True)


def embedded_query(model, query: str) -> np.ndarray:
    return model.encode([query])[0]