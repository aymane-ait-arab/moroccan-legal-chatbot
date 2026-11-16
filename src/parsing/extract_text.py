"""Extrait le texte brut des PDF de data/raw/ vers data/processed/txt/"""
from pathlib import Path
import fitz  # PyMuPDF

RAW = Path("data/raw")
OUT = Path("data/processed/txt")


def extract(pdf_path: Path) -> str:
    doc = fitz.open(pdf_path)
    return "\n".join(page.get_text("text") for page in doc)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for pdf in sorted(RAW.glob("*/*.pdf")):
        text = extract(pdf)
        out = OUT / f"{pdf.stem}.txt"
        out.write_text(text, encoding="utf-8")
        print(f"{pdf.name}: {len(text)} caractères -> {out}")
