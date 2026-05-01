import os

from groq import Groq
from dotenv import load_dotenv

from extraction import extract_all_facts
from comparison import compare_articles

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_articles(folder_path):
    articles = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r") as f:
                articles.append(f.read().strip())
    return articles


def print_articles(articles):
    print("Loaded articles:")
    for i, article in enumerate(articles, start=1):
        print(f"\n--- Article {i} ---\n{article}")


def run_article_pipeline():
    articles = load_articles("data/event1")
    print_articles(articles)


def run_fact_test():
    articles = load_articles("data/event1")
    all_facts = extract_all_facts(articles)
    print("\nExtracted facts per article:")
    for i, facts in enumerate(all_facts, start=1):
        print(f"\n--- Article {i} ---")
        for fact in facts:
            print(f"  - {fact}")


def test_llm_connection():
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Say hello in one sentence."}]
    )
    print("\nLLM connection test:")
    print(response.choices[0].message.content)


def run_comparison():
    articles = load_articles("data/event1")
    report = compare_articles(articles, "event1", client)
    print("\n" + report)
    print("\nReport generated successfully.")


def main():
    run_article_pipeline()
    run_fact_test()
    test_llm_connection()
    run_comparison()

if __name__ == "__main__":
    main()