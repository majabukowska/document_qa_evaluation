from sentence_transformers import SentenceTransformer, util

def evaluate_answer_support(
    answer: str,
    context_chunks: list[str],
    model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    threshold: float = 0.4,
) -> dict:

    model = SentenceTransformer(model_name)

    answer_emb = model.encode(answer, convert_to_tensor=True)
    context_embs = model.encode(context_chunks, convert_to_tensor=True)

    scores = util.cos_sim(answer_emb, context_embs)[0]
    max_score = float(scores.max())

    return {
        "max_similarity": max_score,
        "supported": max_score >= threshold,
    }