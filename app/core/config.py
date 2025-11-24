
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DATABASE_URL: str = "sqlite:///./coworking.db"

    class Config:
        env_file = ".env"

settings = Settings()