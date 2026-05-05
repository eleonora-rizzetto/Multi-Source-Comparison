def format_event_name(event_folder_name):
    name = event_folder_name.replace("_", " ")
    parts = name.split()
    formatted = " ".join(
        part.capitalize() if not part.isdigit() else part
        for part in parts
    )
    return formatted


def count_articles(articles):
    return len(articles)
