# ⚖️ Moroccan Legal Chatbot — RAG System

A bilingual (FR/AR) RAG-powered chatbot for Moroccan law, covering:
- 📘 **Code du Travail** (Loi 65-99) — 586 FR + 164 AR articles
- 👨‍👩‍👧 **Moudawana** (Dahir 1-04-22) — 399 FR + 397 AR articles
- ⚖️ **Dahir des Obligations et Contrats (DOC)** — 1 240 FR + 1 239 AR articles

> **Total indexé : 4 025 articles** prêts pour la recherche vectorielle.

---

## 🏗️ Architecture

```
Question utilisateur
       ↓
[Guardrails] → Hors périmètre ? → Refus poli
       ↓
[BGE-M3 Embedding] → vecteur de la question
       ↓
[ChromaDB] → Top-5 articles les plus pertinents
       ↓
[LLM Gemini / Groq] → Réponse citant loi + article
       ↓
Réponse avec source officielle
```

---

## ✅ Avancement du projet

| Étape | Statut | Détails |
|-------|--------|---------|
| Structure du projet | ✅ Done | Dossiers, Git, GitHub |
| Collecte des données | ✅ Done | 6 PDFs/DOC officiels |
| Parsing des articles | ✅ Done | Parser v3, regex FR + AR |
| Nettoyage JSON | ✅ Done | 4 025 articles propres |
| Indexation ChromaDB | 🔄 À faire | BGE-M3 embeddings |
| Guardrails (refus) | 🔄 À faire | Détecteur hors périmètre |
| RAG Pipeline | 🔄 À faire | Retrieve + Generate |
| Interface Streamlit | 🔄 À faire | Chat + Dashboard |
| Jeu d'évaluation | 🔄 À faire | 40 questions benchmark |
| Métriques RAG | 🔄 À faire | Recall@3, Fidélité, Refus |

---

## 📁 Structure du projet

```
moroccan-legal-chatbot/
├── data/
│   ├── raw/                    # PDFs officiels (non versionnés)
│   │   ├── code_travail/       # code_du_travail_fr.pdf + ar.pdf
│   │   ├── moudawana/          # moudawana_fr.pdf + ar.pdf
│   │   └── doc/                # doc_fr.pdf + doc_ar.doc
│   ├── processed/              # ✅ 6 fichiers JSON (4 025 articles)
│   │   ├── code_travail_fr.json  (586 articles)
│   │   ├── code_travail_ar.json  (164 articles)
│   │   ├── moudawana_fr.json     (399 articles)
│   │   ├── moudawana_ar.json     (397 articles)
│   │   ├── doc_fr.json           (1 240 articles)
│   │   └── doc_ar.json           (1 239 articles)
│   └── vectorstore/            # ChromaDB (non versionné)
├── src/
│   ├── parsing/
│   │   └── parser.py           # ✅ Regex FR + AR, nettoyage, dédup
│   ├── embedding/
│   │   └── indexer.py          # 🔄 BGE-M3 → ChromaDB
│   ├── rag/
│   │   └── pipeline.py         # 🔄 Retrieve + Generate
│   └── guardrails/
│       └── detector.py         # 🔄 Détection hors périmètre
├── app/
│   ├── main.py                 # 🔄 Streamlit entry point
│   └── pages/
│       ├── chat.py             # 🔄 Interface chat bilingue
│       └── dashboard.py        # 🔄 Métriques d'évaluation
├── evaluation/
│   ├── questions/              # 🔄 40 questions benchmark
│   └── results/                # 🔄 Résultats évaluation
├── tests/
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## 🚀 Quick Start

```bash
# 1. Cloner le repo
git clone https://github.com/aymane-ait-arab/moroccan-legal-chatbot.git
cd moroccan-legal-chatbot

# 2. Environnement virtuel
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Dépendances
pip install -r requirements.txt

# 4. Configuration
cp .env.example .env
# Remplir GEMINI_API_KEY ou GROQ_API_KEY dans .env

# 5. Indexer les articles (première fois ~10 min)
python src/embedding/indexer.py --input data/processed/

# 6. Lancer l'app
streamlit run app/main.py
```

---

## 🌿 Stratégie Git (4 personnes)

| Branche | Rôle |
|---------|------|
| `main` | Code stable — merge uniquement via PR validée |
| `develop` | Branche d'intégration |
| `feature/indexation` | Dev 1 — ChromaDB + BGE-M3 |
| `feature/rag-pipeline` | Dev 2 — Pipeline RAG + Guardrails |
| `feature/streamlit-ui` | Dev 3 — Interface Streamlit |
| `feature/evaluation` | Dev 4 — Benchmark 40 questions |

**Workflow :**
```bash
# Chaque dev travaille sur sa branche
git checkout -b feature/ma-feature develop

# Commit régulier
git add .
git commit -m "feat: description claire"
git push origin feature/ma-feature

# Pull Request → develop → review → merge
```

---

## 👥 Répartition des tâches (4 personnes)

| Personne | Module | Fichiers principaux |
|----------|--------|-------------------|
| Dev 1 | Indexation | `src/embedding/indexer.py` |
| Dev 2 | RAG + Guardrails | `src/rag/pipeline.py`, `src/guardrails/detector.py` |
| Dev 3 | Interface | `app/pages/chat.py`, `app/pages/dashboard.py` |
| Dev 4 | Évaluation | `evaluation/questions/`, métriques |

---

## 📄 Licence
MIT
