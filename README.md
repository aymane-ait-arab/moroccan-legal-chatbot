# ⚖️ Moroccan Legal Chatbot — RAG System

A bilingual (FR/AR) RAG-powered chatbot for Moroccan law, covering:
- 📘 **Code du Travail** (Loi 65-99) — 586 FR + 164 AR articles
- 👨‍👩‍👧 **Moudawana** (Dahir 1-04-22) — 399 FR + 397 AR articles
- ⚖️ **Dahir des Obligations et Contrats (DOC)** — 1 240 FR + 1 239 AR articles

> **Total : 4 025 articles parsés et prêts pour l'indexation vectorielle.**

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
| Collecte des données | ✅ Done | 6 PDFs/DOC officiels (FR + AR) |
| Parsing des articles | ✅ Done | Parser v3, regex FR + AR |
| Nettoyage JSON | ✅ Done | 4 025 articles propres |
| Indexation ChromaDB | 🔄 En cours | BGE-M3 embeddings — **Duo 1** |
| Guardrails (refus) | 🔄 En cours | Détecteur hors périmètre — **Duo 1** |
| RAG Pipeline | 🔄 En cours | Retrieve + Generate — **Duo 1** |
| Interface Streamlit | 🔄 En cours | Chat + Dashboard — **Duo 2** |
| Jeu d'évaluation | 🔄 En cours | 40 questions benchmark — **Duo 2** |
| Métriques RAG | 🔄 En cours | Recall@3, Fidélité, Refus — **Duo 2** |

---

## 📁 Structure du projet

```
moroccan-legal-chatbot/
├── data/
│   ├── raw/                      # PDFs officiels (non versionnés)
│   │   ├── code_travail/
│   │   ├── moudawana/
│   │   └── doc/
│   ├── processed/                # ✅ 6 fichiers JSON — 4 025 articles
│   │   ├── code_travail_fr.json  (586 articles)
│   │   ├── code_travail_ar.json  (164 articles)
│   │   ├── moudawana_fr.json     (399 articles)
│   │   ├── moudawana_ar.json     (397 articles)
│   │   ├── doc_fr.json           (1 240 articles)
│   │   └── doc_ar.json           (1 239 articles)
│   └── vectorstore/              # ChromaDB (non versionné)
├── src/
│   ├── parsing/
│   │   └── parser.py             # ✅ Parser v3 — regex FR + AR
│   ├── embedding/
│   │   └── indexer.py            # 🔄 BGE-M3 → ChromaDB [Duo 1]
│   ├── rag/
│   │   └── pipeline.py           # 🔄 Retrieve + Generate [Duo 1]
│   └── guardrails/
│       └── detector.py           # 🔄 Refus hors périmètre [Duo 1]
├── app/
│   ├── main.py                   # 🔄 Streamlit entry point [Duo 2]
│   └── pages/
│       ├── chat.py               # 🔄 Interface chat bilingue [Duo 2]
│       └── dashboard.py          # 🔄 Métriques d'évaluation [Duo 2]
├── evaluation/
│   ├── questions/
│   │   └── benchmark.json        # 🔄 40 questions [Duo 2]
│   └── run_benchmark.py          # 🔄 Script métriques [Duo 2]
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

## 👥 Organisation — 2 Duos

### 🔵 Duo 1 — Backend · branche `feature/backend`

| Développeur | Module | Fichiers |
|-------------|--------|---------|
| Dev A | Indexation ChromaDB + BGE-M3 | `src/embedding/indexer.py` |
| Dev B | RAG Pipeline + Guardrails | `src/rag/pipeline.py`, `src/guardrails/detector.py` |

### 🟣 Duo 2 — Frontend · branche `feature/frontend`

| Développeur | Module | Fichiers |
|-------------|--------|---------|
| Dev C | Interface Streamlit | `app/pages/chat.py`, `app/pages/dashboard.py` |
| Dev D | Évaluation & Benchmark | `evaluation/questions/benchmark.json`, `evaluation/run_benchmark.py` |

---

## 🌿 Git — Instructions par duo

### 🔵 Duo 1 — Premier arrivé crée la branche

```bash
# Dev A — créer et pousser la branche
git clone https://github.com/aymane-ait-arab/moroccan-legal-chatbot.git
cd moroccan-legal-chatbot
git checkout develop
git checkout -b feature/backend
git push -u origin feature/backend

# Dev B — rejoindre la branche
git clone https://github.com/aymane-ait-arab/moroccan-legal-chatbot.git
cd moroccan-legal-chatbot
git fetch origin
git checkout feature/backend
```

```bash
# Workflow quotidien — les deux membres
git pull origin feature/backend    # récupérer le travail de l'autre
# ... coder ...
git add .
git commit -m "feat: description claire"
git push origin feature/backend
```

### 🟣 Duo 2 — Même logique

```bash
# Dev C — créer et pousser la branche
git clone https://github.com/aymane-ait-arab/moroccan-legal-chatbot.git
cd moroccan-legal-chatbot
git checkout develop
git checkout -b feature/frontend
git push -u origin feature/frontend

# Dev D — rejoindre la branche
git clone https://github.com/aymane-ait-arab/moroccan-legal-chatbot.git
cd moroccan-legal-chatbot
git fetch origin
git checkout feature/frontend
```

```bash
# Workflow quotidien — les deux membres
git pull origin feature/frontend   # récupérer le travail de l'autre
# ... coder ...
git add .
git commit -m "feat: description claire"
git push origin feature/frontend
```

### 🔀 Merger dans develop (quand un module est terminé)

```bash
git checkout develop
git pull origin develop
git merge feature/backend          # ou feature/frontend
git push origin develop
```

---

## 📅 Timeline

| Semaine | 🔵 Duo 1 (Backend) | 🟣 Duo 2 (Frontend) |
|---------|-------------------|-------------------|
| **S1** | Indexation ChromaDB | Design UI + Dataset 40 questions |
| **S2** | RAG Pipeline + Guardrails | Intégration pipeline dans UI |
| **S3** | Tests + merge develop | Dashboard métriques + merge develop |
| **S4** | Tests finaux + corrections | Présentation finale |

---

## ⚠️ Règles Git pour tout le monde

- ❌ **Ne jamais pusher directement sur `main`**
- ✅ Toujours `git pull` avant de commencer à coder
- ✅ Commits clairs : `feat:` / `fix:` / `docs:` / `test:`
- ✅ En cas de conflit : ouvrir le fichier, chercher `<<<<<<<`, garder le bon code, puis `git add . && git commit`

---

## 🔑 Accès collaborateurs

Le propriétaire du repo doit ajouter les 3 autres via :
> **GitHub → Settings → Collaborators → Add people**

---

## 📄 Licence
MIT
