"""
Indexing script — embeds parsed articles into ChromaDB using BGE-M3.

Usage:
    python src/embedding/indexer.py --input data/processed/code_travail.json
"""
import json
import chromadb
from pathlib import Path
from sentence_transformers import SentenceTransformer
from tqdm import tqdm


CHROMA_PATH = "./data/vectorstore"
COLLECTION_NAME = "moroccan_law"
MODEL_NAME = "BAAI/bge-m3"


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )
    return collection


def index_articles(json_path: str) -> None:
    """Load parsed articles and add them to ChromaDB."""
    with open(json_path, encoding="utf-8") as f:
        articles = json.load(f)

    print(f"📚 Loading embedding model: {MODEL_NAME}")
    model = SentenceTransformer(MODEL_NAME)
    collection = get_collection()

    texts = [a["texte"] for a in articles]
    metadatas = [{k: v for k, v in a.items() if k != "texte"} for a in articles]
    ids = [f"{a['loi']}_{a['article']}".replace(" ", "_") for a in articles]

    print(f"⚙️  Embedding {len(texts)} articles...")
    embeddings = model.encode(texts, batch_size=32, show_progress_bar=True).tolist()

    collection.upsert(documents=texts, embeddings=embeddings, metadatas=metadatas, ids=ids)
    print(f"✅ Indexed {len(articles)} articles into ChromaDB")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to processed JSON file")
    args = parser.parse_args()
    index_articles(args.input)
