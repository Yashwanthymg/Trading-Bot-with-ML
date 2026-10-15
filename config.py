import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from backend root or app directory
base_dir = Path(__file__).resolve().parent.parent
dotenv_path = base_dir / ".env"
load_dotenv(dotenv_path=dotenv_path)

class Settings:
    PROJECT_NAME: str = "TradeMind AI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api"
    
    # MongoDB
    MONGODB_URL: str = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "trademind_ai")
    
    # Security & JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET", "trademind_ai_super_secret_jwt_key_2026_change_in_production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440")) # 24 hours
    
    # Paper Trading Defaults
    INITIAL_VIRTUAL_CAPITAL: float = float(os.getenv("INITIAL_VIRTUAL_CAPITAL", "100000.0"))
    
    # CORS
    raw_cors = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://localhost:3000,http://127.0.0.1:5173,http://localhost:8000")
    CORS_ORIGINS: list = [origin.strip() for origin in raw_cors.split(",") if origin.strip()]

settings = Settings()
