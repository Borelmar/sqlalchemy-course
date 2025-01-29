from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field

class AppSettings(BaseSettings):
    DB_HOST: str = Field(..., alias="APP_DB_HOST")
    DB_PORT: int = Field(..., alias="APP_DB_PORT")
    DB_USER: str = Field(..., alias="APP_DB_USER")
    DB_PASS: str = Field(..., alias="APP_DB_PASS")
    DB_NAME: str = Field(..., alias="APP_DB_NAME")

    TG_TOKEN: str = Field(..., alias="APP_TG_TOKEN")

    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_prefix = "APP_"
        case_sensitive = True


settings = AppSettings()