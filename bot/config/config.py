from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str
   
    AUTO_TASKS: bool = True

    REF_ID: str = 'ur4c8ftVSBe_bBXPP8EtPQ'

    USE_PROXY_FROM_FILE: bool = True


settings = Settings()


