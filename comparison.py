def compare_articles(articles, event_name, client):
    prompt = f"Here are {len(articles)} articles about the same event: {event_name}.\n"
    prompt += "Identify the main topic discussed in these articles and highlight:\n\n"
    prompt += "1. the shared facts present in all the articles\n"
    prompt += "2. the unique facts which appear only in some of them - state which article each comes from\n"
    prompt += "3. the contradictions between different articles\n\n"
    prompt += "Structure your response with these exact sections:\n"
    prompt += "SHARED FACTS, UNIQUE FACTS, CONTRADICTIONS, SUMMARY.\n\n"
    prompt += "Here are the articles:\n\n"

    for i, article in enumerate(articles, start=1):
        prompt += f"--- Article {i} ---\n{article}\n\n"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
