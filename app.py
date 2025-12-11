import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_community.embeddings import HuggingFaceEmbeddings

# ================== Setup ==================
st.set_page_config(page_title="TheraBot", page_icon="🌿")

load_dotenv()

def get_secret(key: str, default=None):
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.getenv(key, default)

# ===== Env Vars =====
GROQ_API_KEY = get_secret("GROQ_API_KEY")
FAISS_INDEX_PATH = get_secret("FAISS_INDEX_PATH", "data/faiss_index")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY missing. Add it to Streamlit Secrets.")
    st.stop()

# Crisis keywords
CRISIS_KEYWORDS = ["suicide", "kill myself", "end my life", "hopeless", "depressed"]

def check_crisis(text):
    for word in CRISIS_KEYWORDS:
        if word in text.lower():
            return True, "⚠️ If you are in crisis, consider reaching out to a local helpline."
    return False, None

# ============== Load Vector DB ==============
@st.cache_resource
def load_db():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    # Free & local embedding model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    return FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

db = load_db()

# ============== Groq LLM ==================
llm = ChatGroq(
    model="llama3-70b-8192",
    groq_api_key=GROQ_API_KEY,
    temperature=0.7
)

# ============== RAG Function ==================
def get_rag_response(query):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs]) if docs else "No documents found."

    prompt = f"""
You are TheraBot, an empathetic mental wellness assistant.

Context from knowledge base:
{context}

User: {query}

Respond warmly, helpfully, and safely.
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# ============== UI ==================
st.title("🌿 TheraBot (Groq Powered)")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    crisis, helpline_msg = check_crisis(user_input)
    answer = get_rag_response(user_input)

    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", answer))

    if crisis:
        st.session_state.history.append(("bot", helpline_msg))

for role, msg in st.session_state.history:
    st.chat_message(role).write(msg)
