# Multi-Source-Comparison

A Python tool that compares multiple news articles about the same event and generates a structured analysis report.

Given a set of articles, the tool identifies:
- **Shared facts** : information reported consistently across all sources
- **Unique facts** : details that appear in only some articles, with the source noted
- **Contradictions** : claims that conflict between sources
- **Summary** : a brief overall comparison

Reports are generated using the Groq LLM API (llama-3.3-70b-versatile) and saved as Markdown files in the `reports/` folder.