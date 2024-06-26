from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongo_uri: str
    github_oauth_client_id: str
    github_oauth_client_secret: str
    root_path: str = ""
    logging_level: str = "INFO"
    testing: bool = False
    database_url: str = ""
    sync_database_url: str = ""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
