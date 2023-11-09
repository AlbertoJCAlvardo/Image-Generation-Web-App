import os
from dotenv import load_dotenv

env_path = os.path.join(".env")
load_dotenv(env_path)

class Settings:
    api_key = os.getenv('API_KEY')

settings = Settings()
