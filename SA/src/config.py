from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # DSN postgresql+asyncpg://postgres:postgres@localhost:5432/sa_test
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_sqlite(self):
        db_url: str = f"sqlite:///{BASE_DIR}/db.sqlite3"
        return db_url

    @property
    def DATABASE_URL_aiosqlite(self):
        db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
        return db_url

    model_config = SettingsConfigDict(env_file=".env")


setting = Settings()
