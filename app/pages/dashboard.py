"""Dashboard page — evaluation metrics placeholder."""
import streamlit as st

def render_dashboard():
    st.title("📊 Tableau de bord — Évaluation RAG")

    col1, col2, col3 = st.columns(3)
    col1.metric("Recall@3", "—", help="% questions où l'article attendu est dans le Top 3")
    col2.metric("Fidélité", "—", help="Réponse strictement basée sur les articles trouvés")
    col3.metric("Taux de refus correct", "—", help="Questions hors périmètre correctement refusées")

    st.info("Lancez le benchmark depuis `evaluation/run_benchmark.py` pour peupler ce tableau.")
