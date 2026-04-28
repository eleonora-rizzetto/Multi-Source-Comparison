from extraction import extract_facts

def load_articles(path):
    with open(path, "r") as f:
        content = f.read()

    articles = [a.strip() for a in content.split("Article") if a.strip()]
    return articles

def print_articles(articles):
    print("Loaded articles:")
    for i, article in enumerate(articles, start=1):
        print(f"\n--- Article {i} ---\n{article}")

def run_article_pipeline():
    articles = load_articles("data/sample_articles.txt")
    print_articles(articles)

def run_fact_test():
    text = "The sky is blue. It is sunny today. People are happy."
    facts = extract_facts(text)
    print("\nExtracted facts test:")
    print(facts)

def main():
    run_article_pipeline()
    run_fact_test()

if __name__ == "__main__":
    main()