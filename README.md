# Multi-Source-Comparison

A Python tool that compares multiple news articles about the same event and generates a structured analysis report.

Given a set of articles, the tool identifies:
- **Shared facts** : information reported consistently across all sources
- **Unique facts** : details that appear in only some articles, with the source noted
- **Contradictions** : claims that conflict between sources
- **Summary** : a brief overall comparison

Reports are generated using the Groq LLM API (llama-3.3-70b-versatile) and saved as Markdown files in the `reports/` folder.

## Project Structure

```
├── main.py          # Entry point, runs the full pipeline
├── comparison.py    # LLM-based article comparison
├── extraction.py    # Text normalization and fact extraction
├── utils.py         # Utility functions
├── data/            # Input articles, organized by event
├── reports/         # Generated comparison reports
└── tests/           # Unit tests
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root with your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

## Usage

Place article `.txt` files inside subfolders of `data/` (one folder per event):

```
data/
  event1/
    article1.txt
    article2.txt
    article3.txt
```

Then run:

```
python main.py
```

Reports will be saved in the `reports/` folder as Markdown files.