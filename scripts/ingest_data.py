import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

docs_path = "data/"

loaders = [
    DirectoryLoader(docs_path, glob="*.pdf", loader_cls=PyPDFLoader),
    DirectoryLoader(docs_path, glob="*.txt", loader_cls=TextLoader),
    DirectoryLoader(docs_path, glob="*.md", loader_cls=TextLoader),
]

docs = []
for loader in loaders:
    docs.extend(loader.load())

print(f"📄 Loaded {len(docs)} documents")

# SAME model as app.py
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

db = FAISS.from_documents(docs, embeddings)
db.save_local("data/faiss_index")

print("✅ Ingestion complete. FAISS index saved to data/faiss_index")
