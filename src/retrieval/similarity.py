import numpy as np


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denominator = (np.linalg.norm(a) * np.linalg.norm(b))
    if denominator == 0:
        return 0.0
    return float(np.dot(a, b) / denominator)


def rank_by_similarity(query_embedded: np.ndarray, chunks_embedded: np.ndarray) -> list[tuple[int, float]]:
    scores = [(i, cosine_similarity(query_embedded, embedded)) for i, embedded in enumerate(chunks_embedded)]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores