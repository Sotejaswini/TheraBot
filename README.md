🌿 TheraBot

TheraBot is an empathetic, Retrieval-Augmented Generation (RAG) powered therapy-style assistant. It integrates LangChain, FAISS, and Google Gemini models to provide supportive, non-clinical conversations grounded in trusted resources.

⚠️ Disclaimer: TheraBot is not a medical tool and does not provide professional medical advice. For urgent needs, please contact a licensed professional or your regional helpline (e.g., 988 in the US).

🔑 Key Features

RAG with FAISS → Curated knowledge ingestion (PDF, TXT, MD) + contextual retrieval

Gemini LLM Integration → Uses gemini-1.5-flash + text-embedding-004

Safety Guardrails → Crisis keyword detection + helpline suggestion

Unified Streamlit App → Frontend + backend merged for easy deployment

Configurable → .env (local) or st.secrets (Streamlit Cloud)

🛠 Tech Stack

LLM & Embeddings: Google Gemini (gemini-1.5-flash, text-embedding-004)

Vector Store: FAISS

Frameworks: LangChain, Streamlit

Others: dotenv, PyPDFLoader

📂 Project Structure
therabot/
├── app.py                  # Unified Streamlit app (frontend + backend logic)
├── scripts/
│   └── ingest_data.py      # Preprocess docs & build FAISS index
├── data/
│   ├── mental_health_tips.pdf
│   ├── coping_strategies.txt
│   ├── mindfulness.md
│   └── faiss_index/        # auto-created by ingest_data.py
├── requirements.txt
└── README.md

🚀 Quickstart (Local)
1. Clone the repo
git clone https://github.com/Sotejaswini/TheraBot.git
cd TheraBot

2. Create virtual environment & install deps
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Set up .env

Create a file .env:

GEMINI_API_KEY=your_real_key
FAISS_INDEX_PATH=data/faiss_index
LLM_MODEL=gemini-1.5-flash
EMBEDDING_MODEL=models/text-embedding-004

4. Ingest data
python scripts/ingest_data.py


This builds data/faiss_index/.

5. Run Streamlit app
streamlit run app.py


App runs at → http://localhost:8501

☁️ Deploy on Streamlit Cloud

Push repo to GitHub (main branch).

Go to Streamlit Cloud
 → New App.

Select repo → app.py.

Add Secrets under App → Settings → Secrets:

GEMINI_API_KEY="your_real_key"
FAISS_INDEX_PATH="data/faiss_index"
LLM_MODEL="gemini-1.5-flash"
EMBEDDING_MODEL="models/text-embedding-004"


Deploy 🚀

Your app will be live at:
👉 https://sotejaswini-therabot.streamlit.app

💡 Example Prompts

"What are some coping strategies for stress?"

"Give me mindfulness exercises."

"Can you suggest daily routines for mental well-being?"

"I feel hopeless..." → Crisis detection triggers helpline.

📊 Impact

Built a safe, LLM-agnostic conversational AI for mental-health support.

Demonstrates a complete RAG pipeline: ingestion → indexing → retrieval → empathetic response.

Ensures responsible deployment with crisis handling.

FAANG-ready demo: clear, production-style repo + one-click Streamlit deploy.

📌 Resume-Ready Highlights

Developed RAG-based empathetic assistant using LangChain, FAISS, and Google Gemini.

Implemented safety guardrails (crisis detection + helplines) for responsible AI.

Deployed a scalable Streamlit app showcasing real-world LLM integration.

⚠️ Disclaimer

TheraBot is a supportive tool only.
It does not replace professional help. For emergencies, call your local crisis helpline immediately.

Would you like me to also add badges (like “Made with LangChain”, “Deployed on Streamlit”) at the top of the README so it looks even more professional for recruiters?

You said:
yes
ChatGPT said:

Awesome 🚀 — badges give your README a professional, FAANG-ready polish. Here’s your final README.md with badges at the top.

🌿 TheraBot










TheraBot is an empathetic, Retrieval-Augmented Generation (RAG) powered therapy-style assistant. It integrates LangChain, FAISS, and Google Gemini models to provide supportive, non-clinical conversations grounded in trusted resources.

⚠️ Disclaimer: TheraBot is not a medical tool and does not provide professional medical advice. For urgent needs, please contact a licensed professional or your regional helpline (e.g., 988 in the US).

🔑 Key Features

RAG with FAISS → Curated knowledge ingestion (PDF, TXT, MD) + contextual retrieval

Gemini LLM Integration → Uses gemini-1.5-flash + text-embedding-004

Safety Guardrails → Crisis keyword detection + helpline suggestion

Unified Streamlit App → Frontend + backend merged for easy deployment

Configurable → .env (local) or st.secrets (Streamlit Cloud)

🛠 Tech Stack

LLM & Embeddings: Google Gemini (gemini-1.5-flash, text-embedding-004)

Vector Store: FAISS

Frameworks: LangChain, Streamlit

Others: dotenv, PyPDFLoader

📂 Project Structure
therabot/
├── app.py                  # Unified Streamlit app (frontend + backend logic)
├── scripts/
│   └── ingest_data.py      # Preprocess docs & build FAISS index
├── data/
│   ├── mental_health_tips.pdf
│   ├── coping_strategies.txt
│   ├── mindfulness.md
│   └── faiss_index/        # auto-created by ingest_data.py
├── requirements.txt
└── README.md

🚀 Quickstart (Local)
1. Clone the repo
git clone https://github.com/Sotejaswini/TheraBot.git
cd TheraBot

2. Create virtual environment & install deps
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

3. Set up .env

Create a file .env:

GEMINI_API_KEY=your_real_key
FAISS_INDEX_PATH=data/faiss_index
LLM_MODEL=gemini-1.5-flash
EMBEDDING_MODEL=models/text-embedding-004

4. Ingest data
python scripts/ingest_data.py


This builds data/faiss_index/.

5. Run Streamlit app
streamlit run app.py


App runs at → http://localhost:8501

☁️ Deploy on Streamlit Cloud

Push repo to GitHub (main branch).

Go to Streamlit Cloud
 → New App.

Select repo → app.py.

Add Secrets under App → Settings → Secrets:

GEMINI_API_KEY="your_real_key"
FAISS_INDEX_PATH="data/faiss_index"
LLM_MODEL="gemini-1.5-flash"
EMBEDDING_MODEL="models/text-embedding-004"


Deploy 🚀

Your app will be live at:
👉 https://sotejaswini-therabot.streamlit.app

💡 Example Prompts

"What are some coping strategies for stress?"

"Give me mindfulness exercises."

"Can you suggest daily routines for mental well-being?"

"I feel hopeless..." → Crisis detection triggers helpline.

📊 Impact

Built a safe, LLM-agnostic conversational AI for mental-health support.

Demonstrates a complete RAG pipeline: ingestion → indexing → retrieval → empathetic response.

Ensures responsible deployment with crisis handling.

FAANG-ready demo: clear, production-style repo + one-click Streamlit deploy.

📌 Resume-Ready Highlights

Developed RAG-based empathetic assistant using LangChain, FAISS, and Google Gemini.

Implemented safety guardrails (crisis detection + helplines) for responsible AI.

Deployed a scalable Streamlit app showcasing real-world LLM integration.

⚠️ Disclaimer

TheraBot is a supportive tool only.
It does not replace professional help. For emergencies, call your local crisis helpline immediately.


# TheraBot

**TheraBot** is an empathetic, **RAG-powered therapy-style assistant** that integrates **LangChain**, **FAISS**, and **Google Gemini** models to provide supportive, non-clinical conversations grounded in trusted resources.

The system is designed to **ingest knowledge sources** (PDFs, text, Markdown), **embed them with Gemini embeddings**, and **retrieve relevant context** during conversation to reduce hallucinations. A **FastAPI backend** powers the retrieval and response pipeline, while a **Streamlit frontend** provides a user-friendly chat interface.

To ensure safety, TheraBot includes **crisis keyword detection** and automatically displays **regional helplines** when necessary, making it both helpful and responsible.
---

### 🔑 Key Features

* **Retrieval-Augmented Generation (RAG):** Curated knowledge ingestion with FAISS vector database.
* **Gemini LLM Integration:** Uses Google Gemini (`gemini-1.5-flash`) and `text-embedding-004` for embeddings.
* **Safety Guardrails:** Crisis detection with disclaimers and helpline recommendations.
* **FastAPI Backend:** Provides `/chat` and `/health` endpoints.
* **Streamlit UI:** Simple, responsive chat interface with session memory.
* **Configurable:** Environment-based setup for keys, models, and paths.

---

### 🛠️ Tech Stack

* **Backend:** Python, FastAPI, LangChain, FAISS, Google Generative AI SDK
* **Frontend:** Streamlit (chat interface)
* **Testing:** Pytest

---

### 🚀 Impact

* Built an **LLM-agnostic, safe conversational AI** for mental-health support scenarios.
* Demonstrated **end-to-end pipeline**: ingestion → indexing → retrieval → empathetic response.
* Ensured **free-tier accessibility** via Gemini API, lowering entry barriers for experimentation.
* Packaged for **easy deployment and scaling** in real-world environments.
---
