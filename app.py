import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

# Fix Streamlit Cloud inotify issue
os.environ["STREAMLIT_WATCH_IGNORE"] = "true"

# Groq + LangChain
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ===============================
#            SETUP
# ===============================

st.set_page_config(page_title="TheraBot", page_icon="🌿")

load_dotenv()

def get_secret(key: str, default=None):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.getenv(key, default)

# Credentials
GROQ_API_KEY = get_secret("GROQ_API_KEY")
FAISS_INDEX_PATH = get_secret("FAISS_INDEX_PATH", "data/faiss_index")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY missing. Add it in Streamlit Secrets.")
    st.stop()

# Crisis words
CRISIS_KEYWORDS = [
    "suicide", "kill myself", "end my life",
    "hopeless", "can't go on", "depressed"
]

def check_crisis(text: str):
    for w in CRISIS_KEYWORDS:
        if w in text.lower():
            return True, "⚠️ If you feel unsafe or in crisis, please call your local helpline (e.g., 9152987821 in India)."
    return False, None

# ===============================
#     LOAD VECTOR DB
# ===============================

@st.cache_resource
def load_db():
    # Ensure loop for FAISS
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

db = load_db()

# Groq LLM (FREE)
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.1-70b-versatile"
)

# ===============================
#        RAG PIPELINE
# ===============================

def get_rag_response(query: str):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs]) if docs else "No context found."

    prompt = f"""
You are TheraBot, a calm, empathetic mental-health support assistant.
Use the context, but respond kindly and supportively.

Context:
{context}

User: {query}
TheraBot:
"""

    response = llm.invoke(prompt)
    return response.content

# ===============================
#           UI
# ===============================

st.title("🌿 TheraBot — Empathetic AI Companion")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    crisis, help_msg = check_crisis(user_input)
    bot_reply = get_rag_response(user_input)

    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", bot_reply))

    if crisis:
        st.session_state.history.append(("bot", help_msg))

# Chat display
for role, msg in st.session_state.history:
    st.chat_message(role).write(msg)
