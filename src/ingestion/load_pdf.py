from pathlib import Path
import pdfplumber

def load_pdf(path: Path) -> str:
    text = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)

    return "\n".join(text)