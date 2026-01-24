from typing import List, Dict
import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def build_prompt(question: str, contexts: List[Dict]) -> str:
    context_text = "\n\n".join(f"[Source{i}] {c['text']}" for i, c in enumerate(contexts))

    prompt = f"""
You are a question answering assistant.

Answer the question ONLY using the information from the context below.
If the answer is not fully supported by the context, say:
"I don't know based on the provided documents."

Context:
{context_text}

Question:
{question}

Answer:
""".strip()

    return prompt


def generate_answer(question: str, contexts: List[Dict], model: str = "gpt-5-nano") -> Dict:
    prompt = build_prompt(question, contexts)

    if OpenAI is None or not os.getenv("OPENAI_API_KEY"):
        return {
            "answer": "[MOCK] Answer generation skipped (no API key)",
            "prompt": prompt,
            "model": "mock",
        }

    client = OpenAI()

    response = client.responses.create(
        model=model,
        input=prompt,
    )

    answer = response.output_text

    return{
        "answer": answer,
        "prompt": prompt,
        "model": model,
    }