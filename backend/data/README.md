# 📂 Data Folder

This folder contains **knowledge sources** that TheraBot uses for Retrieval-Augmented Generation (RAG).  
These documents are ingested and converted into vector embeddings using **Google Gemini embeddings** + **FAISS**.

## 📄 Contents

- `mental_health_tips.pdf` → A short guide with mental health tips.
- `coping_strategies.txt` → Plain-text coping strategies.
- `mindfulness.md` → A markdown mindfulness guide.

## ⚠️ Notes

- Add your own PDFs, `.txt`, or `.md` files here to extend TheraBot’s knowledge base.
- After adding new files, run:
  ```bash
  python scripts/ingest_data.py
  ```
