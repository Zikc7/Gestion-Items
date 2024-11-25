from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    # ?API
    PORT: int = 8000
    DEV: bool = False

    # ?Logging
    DEBUG: bool = False

    # ?Database
    DB_CONN: str

    class Config:
        env_file = ".env"
