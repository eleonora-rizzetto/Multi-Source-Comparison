import os

from groq import Groq
from dotenv import load_dotenv

from comparison import compare_articles
from utils import format_event_name

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_articles(folder_path):
    articles = []
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    print(f"Warning: {filename} is empty, skipping.")
                    continue
                articles.append(content)
    return articles



def save_report(report, event_name):
    path = f"reports/{event_name}_report.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# Comparison Report - {format_event_name(event_name)}\n\n")
        f.write(report)
    print(f"\nReport generated: {path}")


def run_all_comparisons():
    events = sorted([f for f in os.listdir("data") if os.path.isdir(os.path.join("data", f))])
    for event in events:
        print(f"\nProcessing {event}...")
        articles = load_articles(f"data/{event}")
        if not articles:
            print(f"No articles found in {event}, skipping.")
            continue
        report = compare_articles(articles, event, client)
        save_report(report, event)


def main():
    run_all_comparisons()


if __name__ == "__main__":
    main()