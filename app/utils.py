import os
from dotenv import load_dotenv

def save_summary_to_file(summary: str, file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(summary)

def load_env_variables() -> None:
    load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
