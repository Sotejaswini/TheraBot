# TheraBot

**TheraBot** is an empathetic, **RAG-powered therapy-style assistant** that integrates **LangChain**, **FAISS**, and **Google Gemini** models to provide supportive, non-clinical conversations grounded in trusted resources.

The system is designed to **ingest knowledge sources** (PDFs, text, Markdown), **embed them with Gemini embeddings**, and **retrieve relevant context** during conversation to reduce hallucinations. A **FastAPI backend** powers the retrieval and response pipeline, while a **Streamlit frontend** provides a user-friendly chat interface.

To ensure safety, TheraBot includes **crisis keyword detection** and automatically displays **regional helplines** when necessary, making it both helpful and responsible.

Deployed via **Docker Compose**, the entire stack can be started with a single command, supporting portability and scalability.

---

### 🔑 Key Features

* **Retrieval-Augmented Generation (RAG):** Curated knowledge ingestion with FAISS vector database.
* **Gemini LLM Integration:** Uses Google Gemini (`gemini-1.5-flash`) and `text-embedding-004` for embeddings.
* **Safety Guardrails:** Crisis detection with disclaimers and helpline recommendations.
* **FastAPI Backend:** Provides `/chat` and `/health` endpoints.
* **Streamlit UI:** Simple, responsive chat interface with session memory.
* **Dockerized Deployment:** One-command start with `docker compose`.
* **Configurable:** Environment-based setup for keys, models, and paths.

---

### 🛠️ Tech Stack

* **Backend:** Python, FastAPI, LangChain, FAISS, Google Generative AI SDK
* **Frontend:** Streamlit (chat interface)
* **Infrastructure:** Docker, Docker Compose, dotenv
* **Testing:** Pytest

---

### 🚀 Impact

* Built an **LLM-agnostic, safe conversational AI** for mental-health support scenarios.
* Demonstrated **end-to-end pipeline**: ingestion → indexing → retrieval → empathetic response.
* Ensured **free-tier accessibility** via Gemini API, lowering entry barriers for experimentation.
* Packaged for **easy deployment and scaling** in real-world environments.
---
