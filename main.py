import os

from extraction import extract_facts, extract_all_facts


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

def main():
    run_article_pipeline()
    run_fact_test()

if __name__ == "__main__":
    main()