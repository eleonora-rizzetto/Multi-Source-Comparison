from extraction import extract_facts, extract_all_facts

def load_articles(path):
    with open(path, "r") as f:
        content = f.read()

    articles = [a.strip().split("\n", 1)[-1].strip() for a in content.split("Article") if a.strip()]
    return articles

def print_articles(articles):
    print("Loaded articles:")
    for i, article in enumerate(articles, start=1):
        print(f"\n--- Article {i} ---\n{article}")

def run_article_pipeline():
    articles = load_articles("data/sample_articles.txt")
    print_articles(articles)

def run_fact_test():
    articles = load_articles("data/sample_articles.txt")
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