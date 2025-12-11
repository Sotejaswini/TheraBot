import os
import asyncio
import streamlit as st
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

# Streamlit config
st.set_page_config(page_title="TheraBot", page_icon="🌿")

load_dotenv()

# Secrets / env vars
def get_secret(key, default=None):
    if key in st.secrets:
        return st.secrets[key]
    return os.getenv(key, default)

GROQ_API_KEY = get_secret("GROQ_API_KEY")
FAISS_INDEX_PATH = "data/faiss_index"

if not GROQ_API_KEY:
    st.error("❌ Missing GROQ_API_KEY")
    st.stop()

# Crisis words
CRISIS_WORDS = ["suicide", "kill myself", "end my life", "hopeless", "depressed"]

def check_crisis(text):
    for w in CRISIS_WORDS:
        if w in text.lower():
            return True, "⚠ Please reach your regional helpline if you are in crisis."
    return False, None

@st.cache_resource
def load_db():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

db = load_db()

llm = ChatGroq(
    model_name="mixtral-8x7b-32768",
    groq_api_key=GROQ_API_KEY
)

def get_rag_response(query):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are TheraBot, an empathetic and gentle mental-health assistant.

Context:
{context}

User: {query}
TheraBot:
"""
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# UI
st.title("🌿 TheraBot - Empathetic AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("How are you feeling today?")

if user_input:
    crisis, help_msg = check_crisis(user_input)
    reply = get_rag_response(user_input)

    st.session_state.history.append(("user", user_input))
    st.session_state.history.append(("bot", reply))
    if crisis:
        st.session_state.history.append(("bot", help_msg))

for role, msg in st.session_state.history:
    st.chat_message(role).write(msg)
