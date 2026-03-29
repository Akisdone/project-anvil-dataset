import re
def extract_links(text: str) -> list[dict]:
    text = re.sub(r'`[^`]*`', '', text)
    links = []
    pattern = r'(?<!\!)\[([^\[\]]+)\]\(([^\s)]+)\)'
    for match in re.finditer(pattern, text):
        links.append({
            "text": match.group(1).strip(),
            "url": match.group(2).strip()
        })
    return links