import os

from groq import Groq
from dotenv import load_dotenv

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




def test_llm_connection():
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Say hello in one sentence."}]
    )
    print("\nLLM connection test:")
    print(response.choices[0].message.content)


def save_report(report, event_name):
    path = f"reports/{event_name}_report.md"
    with open(path, "w") as f:
        f.write(f"# Comparison Report - {event_name}\n\n")
        f.write(report)
    print(f"\nReport generated: {path}")


def run_all_comparisons():
    events = sorted([f for f in os.listdir("data") if os.path.isdir(os.path.join("data", f))])
    for event in events:
        print(f"\nProcessing {event}...")
        articles = load_articles(f"data/{event}")
        report = compare_articles(articles, event, client)
        save_report(report, event)


def main():
    run_all_comparisons()

if __name__ == "__main__":
    main()