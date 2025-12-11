import os
import asyncio
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

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

# Env vars
GEMINI_API_KEY = get_secret("GEMINI_API_KEY")
FAISS_INDEX_PATH = get_secret("FAISS_INDEX_PATH", "data/faiss_index")
LLM_MODEL = get_secret("LLM_MODEL", "gemini-1.5-flash")
EMBEDDING_MODEL = get_secret("EMBEDDING_MODEL", "text-embedding-004")  # fixed

if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY missing. Add it to .env or Streamlit Secrets.")
    st.stop()

# Crisis keywords
CRISIS_KEYWORDS = ["suicide", "kill myself", "end my life", "hopeless", "depressed"]

def check_crisis(text: str):
    for word in CRISIS_KEYWORDS:
        if word in text.lower():
            return True, "⚠️ If you are in crisis, please call your regional helpline (e.g., 988 in the US)."
    return False, None

# ================== Load FAISS DB ==================
@st.cache_resource
def load_db():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())

    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GEMINI_API_KEY
    )
    return FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

db = load_db()

# LLM
llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY
)

# ================== FIXED RAG FUNCTION ==================
def get_rag_response(query: str):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs]) if docs else "No relevant documents found."

    prompt = (
        "You are TheraBot, an empathetic mental health assistant.\n"
        "Use the following context to help the user, but DO NOT mention the documents.\n"
        "Always be supportive, calm, human-like, and gentle.\n\n"
        f"Context:\n{context}\n\n"
        f"User: {query}\n"
        "TheraBot:"
    )

    # ✅ Correct and required for Gemini
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# ================== Streamlit UI ==================
st.title("🌿 TheraBot - Empathetic AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    crisis, helpline = check_crisis(user_input)
    answer = get_rag_response(user_input)

    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", answer))

    if crisis:
        st.session_state.history.append(("bot", helpline))

# Render chat
for role, msg in st.session_state.history:
    st.chat_message(role).write(msg)
