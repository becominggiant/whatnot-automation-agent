import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./whatnot.db")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
APP_ENV = os.getenv("APP_ENV", "development")
