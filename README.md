# 🌿 TheraBot

[![Made with LangChain](https://img.shields.io/badge/Made%20with-LangChain-blue)](https://www.langchain.com/)  
[![Deployed on Streamlit](https://img.shields.io/badge/Deployed%20on-Streamlit-brightgreen)](https://sotejaswini-therabot.streamlit.app)  
[![Powered by Google Gemini](https://img.shields.io/badge/Powered%20by-Google%20Gemini-orange)](https://deepmind.google/technologies/gemini/)  

TheraBot is an empathetic, Retrieval-Augmented Generation (RAG) powered therapy-style assistant.  
It integrates **LangChain**, **FAISS**, and **Google Gemini models** to provide supportive, non-clinical conversations grounded in trusted resources.

> ⚠️ **Disclaimer**  
> TheraBot is **not a medical tool** and does not provide professional medical advice.  
> For urgent needs, please contact a licensed professional or your regional helpline (e.g., **988** in the US).

---

## 🔑 Key Features
- **RAG with FAISS** → Curated knowledge ingestion (PDF, TXT, MD) + contextual retrieval  
- **Gemini LLM Integration** → Uses `gemini-1.5-flash` + `text-embedding-004`  
- **Safety Guardrails** → Crisis keyword detection + helpline suggestion  
- **Unified Streamlit App** → Frontend + backend merged for easy deployment  
- **Configurable** → `.env` (local) or `st.secrets` (Streamlit Cloud)  

---

## 🛠 Tech Stack
- **LLM & Embeddings**: Google Gemini (`gemini-1.5-flash`, `text-embedding-004`)  
- **Vector Store**: FAISS  
- **Frameworks**: LangChain, Streamlit  
- **Others**: dotenv, PyPDFLoader  

---

## 📂 Project Structure
```
therabot/
├── app.py # Unified Streamlit app (frontend + backend logic)
├── scripts/
│ └── ingest_data.py # Preprocess docs & build FAISS index
├── data/
│ ├── mental_health_tips.pdf
│ ├── coping_strategies.txt
│ ├── mindfulness.md
│ └── faiss_index/ # Auto-created by ingest_data.py
├── requirements.txt
└── README.md
```


---

## 🚀 Quickstart (Local)

1. **Clone the repo**
   ```bash
   git clone https://github.com/Sotejaswini/TheraBot.git
   cd TheraBot

2. **Create virtual environment & install deps**
```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```
3. **Set up .env**
Create a file named .env:
```
GEMINI_API_KEY=your_real_key
FAISS_INDEX_PATH=data/faiss_index
LLM_MODEL=gemini-1.5-flash
EMBEDDING_MODEL=models/text-embedding-004
```
4. **Ingest data**
```bash
python scripts/ingest_data.py
```
This builds data/faiss_index/.

5. **Run Streamlit app**
```bash
streamlit run app.py
```
- App runs at → http://localhost:8501
---

## ☁️ Deploy on Streamlit Cloud

- Push repo to GitHub (main branch).

- Go to Streamlit Cloud
 → New App.

- Select repo → app.py.

- Add Secrets under App → Settings → Secrets:
```bash
GEMINI_API_KEY="your_real_key"
FAISS_INDEX_PATH="data/faiss_index"
LLM_MODEL="gemini-1.5-flash"
EMBEDDING_MODEL="models/text-embedding-004"
```

## Deploy 🚀

- Your app will be live at: 👉 https://sotejaswini-therabot.streamlit.app

## 💡 Example Prompts

- "What are some coping strategies for stress?"

- "Give me mindfulness exercises."

- "Can you suggest daily routines for mental well-being?"

- "I feel hopeless..."
  → (Crisis detection triggers helpline)
  
  ---

### 📊 Impact

- Built a safe, LLM-agnostic conversational AI for mental-health support.

- Demonstrates a complete RAG pipeline: ingestion → indexing → retrieval → empathetic response.

- Ensures responsible deployment with crisis handling.

---
### ⚠️ Disclaimer

- TheraBot is a supportive tool only.
- It does not replace professional help.
- For emergencies, call your local crisis helpline immediately.
---
## License

This project is licensed under the MIT License.

