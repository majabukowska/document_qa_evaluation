def split_by_words(words, max_words, overlap):
    chunks = []
    start = 0

    while start < len(words):
        end = start + max_words
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        start = end - overlap if overlap > 0 else end

        if start < 0:
            start = 0

    return chunks


def chunk_text(text: str, source: str, max_words: int = 500, overlap: int = 50):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    chunk_id = 0

    for paragraph in paragraphs:
        words = paragraph.split()

        if len(words) > max_words:
            sub_chunks = split_by_words(words, max_words, overlap)
            for sub in sub_chunks:
                chunks.append({
                    "id": chunk_id,
                    "chunk_index": chunk_id,
                    "text": sub,
                    "source": source,
                    "word_count": len(sub.split()),
                    "split_type": "word_split",
                })

                chunk_id += 1
            continue

        chunks.append({
            "id": chunk_id,
            "chunk_index": chunk_id,
            "text": paragraph,
            "source": source,
            "word_count": len(paragraph.split()),
            "split_type": "paragraph",
        })

        chunk_id += 1

    return chunks