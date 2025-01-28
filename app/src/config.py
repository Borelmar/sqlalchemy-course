from pydantic_settings import BaseSettings, SettingsConfigDict

class DBSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgres+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB.NAME}"

    class Config:
        env_prefix = "DB_"

db_settings = DBSettings()