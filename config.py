from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    insta_username: str
    insta_password: str

    class Config:
        env_file=".env"


settings = Settings()