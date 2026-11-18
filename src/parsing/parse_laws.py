"""
Découpe les textes français extraits (data/processed/txt/*.txt)
en articles et les enregistre en JSON (1 article = 1 entrée).

Usage (depuis la racine du projet) :
    python src/parsing/parse_laws.py
"""
import json
import re
from pathlib import Path

TXT = Path("data/processed/txt")
OUT = Path("data/processed")

# fichier texte -> (fichier JSON de sortie, nom de la loi, domaine)
LOIS = {
    "code_du_travail_fr": ("code_travail_fr", "Code du Travail", "droit_travail"),
    "moudawana_fr": ("moudawana_fr", "Moudawana", "droit_famille"),
    "doc_fr": ("doc_fr", "DOC", "droit_civil"),
}

# "Article 231" seul sur sa ligne (ancré au début de ligne : on ignore
# les renvois du genre "conformément à l'article 52")
HEADER = re.compile(
    r"^[ \t]*Article[ \t]+(premier|\d+(?:-\d+)?(?:[ \t]+(?:bis|ter|quater))?)[ \t]*$",
    re.M | re.I,
)
PAGE = re.compile(r"^[ \t]*-\s*\d+\s*-[ \t]*$", re.M)  # lignes "- 6 -"


def fix_number(raw: str, prev: int | None) -> str:
    """Le PDF colle parfois un numéro de note au numéro d'article
    (ex. 'Article 25635' = article 256 + note 35). On corrige avec la
    suite logique des numéros."""
    raw = re.sub(r"\s+", " ", raw.strip())
    if raw.lower() == "premier":
        return "1"
    if raw.isdigit() and prev is not None:
        if raw == str(prev + 1):
            return raw
        for k in range(prev + 1, prev + 6):
            if raw.startswith(str(k)) and len(raw) > len(str(k)):
                return str(k)
    return raw


def parse(text: str, loi: str, domaine: str, langue: str = "fr") -> list[dict]:
    text = PAGE.sub("", text)
    matches = list(HEADER.finditer(text))
    articles, prev, seen, dropped = [], None, set(), []
    for i, m in enumerate(matches):
        num = fix_number(m.group(1), prev)
        if num.isdigit() and (prev is None or prev < int(num) <= prev + 60):
            prev = int(num)
        if num in seen:  # doublon (ex. texte d'une loi modificative) : on garde le 1er
            dropped.append(num)
            continue
        seen.add(num)
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = re.sub(r"[ \t]+\n", "\n", text[m.end():end]).strip()
        articles.append({
            "id": f"{domaine}_art_{num.replace(' ', '_')}",
            "loi": loi,
            "article": f"Art. {num}",
            "texte": body,
            "langue": langue,
            "domaine": domaine,
        })
    if dropped:
        print(f"   doublons ignorés : {len(dropped)} {dropped[:10]}")
    return articles


if __name__ == "__main__":
    for stem, (name, loi, domaine) in LOIS.items():
        text = (TXT / f"{stem}.txt").read_text(encoding="utf-8")
        arts = parse(text, loi, domaine)
        out = OUT / f"{name}.json"
        out.write_text(json.dumps(arts, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{loi}: {len(arts)} articles -> {out}")
