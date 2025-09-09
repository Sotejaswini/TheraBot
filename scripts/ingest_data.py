import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load .env file from configs/
load_dotenv("configs/.env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment")

docs_path = "data/"

# Load docs
loaders = [
    DirectoryLoader(docs_path, glob="*.pdf", loader_cls=PyPDFLoader),
    DirectoryLoader(docs_path, glob="*.txt", loader_cls=TextLoader),
    DirectoryLoader(docs_path, glob="*.md", loader_cls=TextLoader),
]

docs = []
for loader in loaders:
    docs.extend(loader.load())

print(f"📄 Loaded {len(docs)} documents")

# Build embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    google_api_key=GEMINI_API_KEY
)

db = FAISS.from_documents(docs, embeddings)
db.save_local("data/faiss_index")

print("✅ Ingestion complete. FAISS index saved to data/faiss_index")
