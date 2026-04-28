import re

def extract_facts(text):
    sentences = re.split(r'[.!?]', text)
    facts = [s.strip().lower() for s in sentences if s.strip()]
    return facts