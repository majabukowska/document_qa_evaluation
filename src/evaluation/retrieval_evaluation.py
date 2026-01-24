from src.retrieval.search import search

def evaluate_retrieval(index: dict, evaluation_data: list[dict], k: int = 5) -> dict:
    hits = 0
    reciprocal_ranks = []

    for sample in evaluation_data:
        query = sample["query"]
        expected_source = sample["expected_source"]

        results = search(index, query, k=k)

        found = False

        for rank, r in enumerate(results, start=1):
            if r["source"] == expected_source:
                hits += 1
                reciprocal_ranks.append(1 / rank)
                found = True
                break

        if not found:
            reciprocal_ranks.append(0.0)
    total = len(evaluation_data)

    return {
        "hit_at_k": hits / total if total else 0.0,
        "mrr": sum(reciprocal_ranks) / total if total else 0.0,
        "samples": total,
        "k": k
    }
