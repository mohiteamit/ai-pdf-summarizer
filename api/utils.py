import os
from dotenv import load_dotenv

def load_env_variables() -> None:
    load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")