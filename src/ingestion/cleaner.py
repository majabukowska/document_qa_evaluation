import re


GENERIC_BLACKLIST_PHRASES = [
    "log in",
    "sign in",
    "sign up",
    "create account",
    "my account",
    "account information",
    "subscribe",
    "newsletter",
    "thank you for subscribing",
    "get updates",
    "privacy policy",
    "privacy statement",
    "terms of service",
    "cookie policy",
    "cookie preferences",
    "skip to content",
    "back to top",

    #roles
    "writer",
    "editor",
    "author",
    "staff",
]


def remove_blacklist_phrases(text: str) -> str:
    for phrase in GENERIC_BLACKLIST_PHRASES:
        text = re.sub(
            rf"\b{re.escape(phrase)}\b",
            "",
            text,
            flags=re.IGNORECASE,
        )

    return text


def normalize_whitespace(text: str) -> str:
    lines = [
        line.strip()
        for line in text.splitlines()
        if len(line.strip()) > 3
    ]
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def is_like_content(line: str) -> bool:
    if len(line) < 30:
        return False

    alpha_ratio = sum(c.isalpha() for c in line) / len(line)
    if alpha_ratio < 0.6:
        return False

    return True

def merge_lines_into_paragraphs(text: str) -> str:
    paragraphs = []
    buffer =[]

    for line in text.splitlines():
        if line.strip():
            buffer.append(line.strip())
        else:
            if buffer:
                paragraphs.append("".join(buffer))
                buffer = []
    if buffer:
        paragraphs.append("".join(buffer))

    return "\n\n".join(paragraphs)


def filter_content_lines(text: str) -> str:
    lines = [
        line for line in text.splitlines()
        if is_like_content(line)
    ]

    return "\n".join(lines)

def fix_split_words(text: str) -> str:
    pattern = r"\b([A-Z][a-z]{0,4})\s+([A-Z][a-z]{2,})\b"

    def merge(match):
        left, right = match.group(1), match.group(2)
        if len(left) <= 4 and len(right) <= 12:
            return left + right

        return match.group(0)

    return re.sub(pattern, merge, text)

def postprocess_text(text: str) -> str:
    text = re.sub(r"\.(?=[A-Z])", ". ", text)
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    text = re.sub(r"([a-zA-Z])\(", r"\1 (", text)
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"\(cid:\d+\)", "", text)

    return text.strip()

def clean_text(text: str) -> str:
    text = normalize_whitespace(text)
    text = remove_blacklist_phrases(text)
    text = filter_content_lines(text)
    text = merge_lines_into_paragraphs(text)
    text = postprocess_text(text)
    text = fix_split_words(text)

    return text.strip()