from pathlib import Path

from .load_html import load_html
from .load_pdf import load_pdf
from .load_docx import load_docx

def load_document(path: Path) -> str:
    suffix = path.suffix.lower()

    if suffix == ".html" or suffix == ".htm":
        return load_html(path)
    elif suffix == ".pdf":
        return load_pdf(path)
    elif suffix == ".docx":
        return load_docx(path)
    elif suffix == ".txt":
        return path.read_text(encoding="utf-8")
    else:
        raise ValueError(f"Unknown document format: {suffix}")
