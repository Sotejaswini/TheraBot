import os
from dotenv import load_dotenv
from pathlib import Path

# Project root (two levels up from backend/)
BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / "configs" / ".env"

print(f"📂 Looking for .env at: {ENV_PATH}")

# Load .env
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    print("⚠️ .env file not found!")

class Settings:
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    FAISS_INDEX_PATH: str = os.getenv("FAISS_INDEX_PATH", "data/faiss_index")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gemini-1.5-flash")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "models/text-embedding-004")

settings = Settings()

print(f"🔑 GEMINI_API_KEY loaded? {'Yes' if settings.GEMINI_API_KEY else 'No'}")
