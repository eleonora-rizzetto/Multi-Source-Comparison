from extraction import normalise_text, extract_facts, extract_all_facts


def test_normalise_text_lowercases():
    assert normalise_text("Hello World") == "hello world"


def test_normalise_text_removes_punctuation():
    assert normalise_text("Hello, World!") == "hello world"


def test_normalise_text_collapses_spaces():
    assert normalise_text("hello   world") == "hello world"


def test_normalise_text_strips_whitespace():
    assert normalise_text("  hello  ") == "hello"


def test_extract_facts_splits_on_period():
    facts = extract_facts("The sky is blue. The grass is green.")
    assert len(facts) == 2


def test_extract_facts_splits_on_question_mark():
    facts = extract_facts("Is it raining? Yes it is.")
    assert len(facts) == 2


def test_extract_facts_ignores_empty_sentences():
    facts = extract_facts("Hello. . World.")
    assert all(f != "" for f in facts)


def test_extract_facts_returns_normalised_text():
    facts = extract_facts("The Sky Is BLUE.")
    assert facts[0] == "the sky is blue"


def test_extract_all_facts_returns_one_list_per_article():
    articles = ["The sky is blue.", "The grass is green. It is soft."]
    result = extract_all_facts(articles)
    assert len(result) == 2


def test_extract_all_facts_correct_fact_count():
    articles = ["The sky is blue. The sun is bright.", "The grass is green."]
    result = extract_all_facts(articles)
    assert len(result[0]) == 2
    assert len(result[1]) == 1
