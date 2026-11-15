# 🏛️ Moroccan Legal Chatbot — RAG System

A bilingual (FR/AR) RAG-powered chatbot for Moroccan law, covering:
- 📘 Code du Travail (Loi 65-99)
- 👨‍👩‍👧 Moudawana (Dahir 1-04-22)
- ⚖️ Dahir des Obligations et Contrats (DOC)
- *(Extensible to all Moroccan law)*

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/moroccan-legal-chatbot.git
cd moroccan-legal-chatbot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and add your API keys

# 5. Run the app
streamlit run app/main.py
```

## 📁 Project Structure

```
moroccan-legal-chatbot/
├── data/
│   ├── raw/              # Raw PDF/TXT law files (not versioned)
│   ├── processed/        # Parsed articles as JSON
│   └── vectorstore/      # ChromaDB index (not versioned)
├── src/
│   ├── parsing/          # Regex article extractors
│   ├── embedding/        # BGE-M3 indexing scripts
│   ├── rag/              # RAG pipeline
│   └── guardrails/       # Out-of-scope detection
├── app/
│   ├── main.py           # Streamlit entry point
│   ├── pages/            # Chat & Dashboard pages
│   └── components/       # UI components
├── evaluation/
│   ├── questions/        # 40-question benchmark dataset
│   └── results/          # Evaluation outputs
└── tests/                # Unit tests
```

## 🌿 Branching Strategy

| Branch | Purpose |
|--------|---------|
| `main` | Stable, production-ready code |
| `develop` | Integration branch — merge features here first |
| `feature/xxx` | New features (e.g. `feature/parsing-moudawana`) |
| `fix/xxx` | Bug fixes |

## 👥 Team

- **Dev 1** — Data pipeline (parsing + embedding)
- **Dev 2** — App interface (Streamlit + evaluation)

## 📄 License
MIT
