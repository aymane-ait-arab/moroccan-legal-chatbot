"""
Moroccan Legal Chatbot - Main Streamlit App
Run with: streamlit run app/main.py
"""
import streamlit as st

st.set_page_config(
    page_title="Chatbot Juridique Marocain",
    page_icon="⚖️",
    layout="wide"
)

st.sidebar.title("⚖️ Chatbot Juridique")
st.sidebar.markdown("**Droit Marocain — RAG System**")

page = st.sidebar.radio("Navigation", ["💬 Assistant", "📊 Tableau de bord"])

if page == "💬 Assistant":
    from pages.chat import render_chat
    render_chat()
elif page == "📊 Tableau de bord":
    from pages.dashboard import render_dashboard
    render_dashboard()
