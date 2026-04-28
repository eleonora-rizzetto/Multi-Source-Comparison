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

def main():
    articles = load_articles("data/sample_articles.txt")
    print_articles(articles)

if __name__ == "__main__":
    main()