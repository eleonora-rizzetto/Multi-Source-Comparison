import re


def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_facts(text):
    sentences = re.split(r'[.!?]', text)

    facts = []
    for s in sentences:
        s = normalize_text(s)
        if s:
            facts.append(s)

    return facts