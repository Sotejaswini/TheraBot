import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI

# ================== Setup ==================
st.set_page_config(page_title="TheraBot", page_icon="🌿")

# Load env (for local runs) or Streamlit secrets (cloud)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", st.secrets.get("GEMINI_API_KEY"))
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "data/faiss_index")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-1.5-flash")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "models/text-embedding-004")

if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY missing. Please add it to .env (local) or Streamlit secrets (cloud).")
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

llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GEMINI_API_KEY
)

def get_rag_response(query: str):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs]) if docs else "No relevant docs found."
    prompt = f"Context:\n{context}\n\nUser: {query}\nTheraBot:"
    return llm.invoke(prompt).content

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

for role, msg in st.session_state.history:
    st.chat_message(role).write(msg)
