from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from app.core.config import settings

def _init_embeddings():
    if not settings.GEMINI_API_KEY:
        raise ValueError("❌ GEMINI_API_KEY missing in configs/.env")
    return GoogleGenerativeAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        google_api_key=settings.GEMINI_API_KEY
    )

def _init_llm():
    if not settings.GEMINI_API_KEY:
        raise ValueError("❌ GEMINI_API_KEY missing in configs/.env")
    return ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=settings.GEMINI_API_KEY
    )

embeddings = _init_embeddings()
llm = _init_llm()

# ✅ Allow safe FAISS pickle load
db = FAISS.load_local(
    settings.FAISS_INDEX_PATH,
    embeddings,
    allow_dangerous_deserialization=True
)

def get_rag_response(query: str, session_id: str = "default"):
    docs = db.similarity_search(query, k=3)
    context = "\n".join([d.page_content for d in docs]) if docs else "No relevant docs found."
    prompt = f"Context:\n{context}\n\nUser: {query}\nTheraBot:"
    return llm.invoke(prompt).content
