"""
RAG Pipeline — retrieves relevant articles and generates answers via LLM.
"""
import os
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = "./data/vectorstore"
COLLECTION_NAME = "moroccan_law"
MODEL_NAME = "BAAI/bge-m3"
TOP_K = 5


class RAGPipeline:
    def __init__(self):
        print("🔄 Loading RAG pipeline...")
        self.model = SentenceTransformer(MODEL_NAME)
        self.client = chromadb.PersistentClient(path=CHROMA_PATH)
        self.collection = self.client.get_collection(COLLECTION_NAME)
        self._load_llm()

    def _load_llm(self):
        """Initialize LLM client (Gemini by default)."""
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.llm = genai.GenerativeModel("gemini-1.5-flash")

    def retrieve(self, query: str, lois: list[str] = None, top_k: int = TOP_K) -> list[dict]:
        """Find the most relevant articles for a given query."""
        query_embedding = self.model.encode(query).tolist()

        where_filter = {"loi": {"$in": lois}} if lois else None

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=where_filter,
            include=["documents", "metadatas", "distances"]
        )

        articles = []
        for doc, meta, dist in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            articles.append({"texte": doc, "score": 1 - dist, **meta})
        return articles

    def generate(self, query: str, articles: list[dict], langue: str = "fr") -> str:
        """Generate a grounded answer using retrieved articles."""
        context = "\n\n".join(
            f"[{a['loi']} — {a['article']}]\n{a['texte']}" for a in articles
        )

        prompt = f"""Tu es un assistant juridique spécialisé dans le droit marocain.
Réponds UNIQUEMENT en te basant sur les articles de loi ci-dessous.
Cite toujours la loi et le numéro d'article dans ta réponse.
Si la question demande un avis personnel ou une estimation de chances, refuse poliment.

--- Articles trouvés ---
{context}

--- Question de l'utilisateur ---
{query}

--- Réponse ({langue}) ---"""

        response = self.llm.generate_content(prompt)
        return response.text

    def answer(self, query: str, lois: list[str] = None, langue: str = "fr") -> dict:
        """Full RAG pipeline: retrieve + generate."""
        articles = self.retrieve(query, lois=lois)
        response = self.generate(query, articles, langue=langue)
        return {"response": response, "sources": articles}
