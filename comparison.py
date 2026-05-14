import json


def compare_articles(articles, event_name, client):
    prompt = f"Here are {len(articles)} articles about the same event: {event_name}.\n"
    prompt += "Analyze the articles and return a JSON object with exactly these four keys:\n\n"
    prompt += '- "shared_facts": a list of strings, each being a fact present in all articles\n'
    prompt += '- "unique_facts": a dict mapping each article identifier (e.g. "Article 1") to a list of strings, each being a fact unique to that article\n'
    prompt += '- "contradictions": a list of strings, each describing a contradiction between articles\n'
    prompt += '- "summary": a single string summarizing the overall comparison\n\n'
    prompt += "Return only the JSON object, no extra text, no markdown formatting.\n\n"
    prompt += "Here are the articles:\n\n"

    for i, article in enumerate(articles, start=1):
        prompt += f"--- Article {i} ---\n{article}\n\n"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    return json.loads(raw)
