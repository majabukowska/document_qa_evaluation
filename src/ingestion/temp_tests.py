import json
from pathlib import Path

from src.ingestion.loader import load_document
from src.ingestion.cleaner import clean_text
from src.ingestion.chunker import chunk_text

from src.retrieval.search import build_index, search
from src.evaluation.retrieval_evaluation import evaluate_retrieval
from src.api.generator import generate_answer
from src.evaluation.answer_eval import evaluate_answer_support


# -----------------------
# INGESTION
# -----------------------
raw = load_document(Path("data/raw/What is PyTorch_ _ IBM.html"))
cleaned = clean_text(raw)
chunks = chunk_text(
    cleaned,
    source="IBM PyTorch",
    max_words=400,
    overlap=50,
)

index = build_index(chunks)


# -----------------------
# RETRIEVAL EVALUATION
# -----------------------
with open("data/evaluation/retrieval_evaluation.json", "r", encoding="utf-8") as f:
    evaluation_data = json.load(f)

metrics = evaluate_retrieval(index, evaluation_data, k=3)

print("\n=== RETRIEVAL EVALUATION ===")
for k, v in metrics.items():
    print(f"{k}: {v}")


# -----------------------
# RETRIEVAL (ACTUAL CONTEXT)
# -----------------------
print("\n=== RETRIEVED CONTEXT ===")

query = "What is PyTorch?"
results = search(index, query, k=3)

for r in results:
    print("\n---")
    print(f"score={r['score']:.3f} source={r['source']} chunk={r['chunk_index']}")
    print(r["text"][:300])


# -----------------------
# ANSWER GENERATION
# -----------------------
print("\n=== ANSWER GENERATION ===")

answer_result = generate_answer(
    question=query,
    contexts=results,
)

answer_text = answer_result["answer"]

print("\nAnswer:")
print(answer_text)


# -----------------------
# ANSWER EVALUATION
# -----------------------
context_texts = [r["text"] for r in results]

answer_eval = evaluate_answer_support(
    answer=answer_text,
    context_chunks=context_texts,
)

print("\n=== ANSWER EVALUATION ===")
for k, v in answer_eval.items():
    print(f"{k}: {v}")
