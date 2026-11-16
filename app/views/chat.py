"""Chat page — placeholder until RAG pipeline is connected."""
import streamlit as st

def render_chat():
    st.title("💬 Assistant Juridique Marocain")
    st.caption("Posez votre question sur le droit marocain.")

    # Language + filter controls
    col1, col2 = st.columns([1, 3])
    with col1:
        lang = st.selectbox("Langue", ["Français", "العربية"])
    with col2:
        lois = st.multiselect(
            "Filtrer par loi",
            ["Code du Travail", "Moudawana", "DOC"],
            default=["Code du Travail", "Moudawana", "DOC"]
        )

    st.divider()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Votre question juridique..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # TODO: replace with real RAG call
            response = "⚙️ Le moteur RAG est en cours de développement. Revenez bientôt !"
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.warning("⚠️ Cet assistant fournit des informations juridiques générales. "
               "Il ne remplace pas l'avis d'un avocat.")
