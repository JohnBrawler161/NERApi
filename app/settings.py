from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    reload: bool

    openai_key: str

    class Config:
        extra = "allow"
        env_file = ".env"


settings = Settings()
