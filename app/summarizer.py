from app.utils import *
from openai import OpenAI

load_env_variables()
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_summary(text: str, 
                     summary_type: str = "Brief", 
                     model: str = "gpt-3.5-turbo", 
                     max_tokens: int = 300, 
                     temperature: float = 0.5) -> str:
    max_chunk_size = 4000
    chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    summaries = []
    for chunk in chunks:
        prompt = f"Summarize in a {summary_type.lower()} manner: {chunk}"
        response = client.chat.completions.create(
            model=model,  # Dynamic model selection
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,  # Dynamic max tokens
            temperature=temperature  # Dynamic temperature
        )
        summaries.append(response.choices[0].message.content.strip())
    return "\n".join(summaries)
