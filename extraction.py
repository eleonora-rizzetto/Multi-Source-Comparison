import re


def normalise_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_facts(text):
    sentences = re.split(r'[.!?]', text)

    facts = []
    for s in sentences:
        s = normalise_text(s)
        if s:
            facts.append(s)

    return facts


def extract_all_facts(articles):
    all_facts = []
    for article in articles:
        facts = extract_facts(article)
        all_facts.append(facts)
    return all_facts