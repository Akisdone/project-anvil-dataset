# Task: Markdown Link Extractor
Implement a function `extract_links(text: str) -> list[dict]` that finds Markdown links `[text](url)`.
- Do NOT extract links inside backticks (code blocks).
- Return a list of dicts: {"text": "...", "url": "..."}.