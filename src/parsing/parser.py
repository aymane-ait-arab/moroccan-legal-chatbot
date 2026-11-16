"""
Article parser for Moroccan law texts.
Extracts articles using regex — 1 article = 1 chunk.

Usage:
    python src/parsing/parser.py --input data/raw/code_travail/ --output data/processed/
"""
import re
import json
from pathlib import Path


# Regex patterns for French and Arabic article headers
PATTERNS = {
    "fr": r"(?:Article\s+(\d+(?:\s*bis)?)\s*[:\-–]?)(.*?)(?=Article\s+\d+|$)",
    "ar": r"(?:المادة\s+(\d+))(.*?)(?=المادة\s+\d+|$)",
}


def parse_articles(text: str, loi: str, langue: str = "fr") -> list[dict]:
    """Extract articles from raw text and return structured chunks."""
    pattern = PATTERNS.get(langue, PATTERNS["fr"])
    matches = re.findall(pattern, text, re.DOTALL)

    articles = []
    for num, content in matches:
        content = content.strip()
        if len(content) < 20:   # skip empty/corrupt matches
            continue
        articles.append({
            "loi": loi,
            "article": f"Art. {num.strip()}",
            "texte": content,
            "langue": langue,
            "domaine": _detect_domain(loi),
        })
    return articles


def _detect_domain(loi: str) -> str:
    """Map law name to legal domain."""
    mapping = {
        "Code du Travail": "droit_travail",
        "Moudawana": "droit_famille",
        "DOC": "droit_civil",
        "Code Pénal": "droit_penal",
        "Code de Commerce": "droit_commercial",
    }
    for key, domain in mapping.items():
        if key.lower() in loi.lower():
            return domain
    return "autre"


def save_articles(articles: list[dict], output_path: str) -> None:
    """Save parsed articles as JSON."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved {len(articles)} articles → {output_path}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to raw text file")
    parser.add_argument("--loi", required=True, help="Law name (e.g. 'Code du Travail')")
    parser.add_argument("--output", required=True, help="Output JSON file path")
    parser.add_argument("--langue", default="fr", choices=["fr", "ar"])
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        raw_text = f.read()

    articles = parse_articles(raw_text, args.loi, args.langue)
    save_articles(articles, args.output)
