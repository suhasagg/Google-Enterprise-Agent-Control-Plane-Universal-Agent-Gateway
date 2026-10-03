from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
 database_url:str="postgresql+asyncpg://postgres:postgres@localhost:5432/agents";redis_url:str="redis://localhost:6379/0";api_key:str="change-me";kafka_bootstrap:str="localhost:9092";mcp_mode:str="mock";a2a_mode:str="mock";rest_mode:str="mock"
 model_config=SettingsConfigDict(env_file=".env",extra="ignore")
settings=Settings()
