from pydantic import BaseModel
from openai import OpenAI
from new_app.config import get_client

class BookRecommendation(BaseModel):
    title: str
    author: str
    genre: str
    reading_time_minutes: int

client = get_client("OpenRouter")

response = client.beta.chat.completions.parse(
    model="openai/gpt-6-luna",
    messages=[
        {"role": "system", "content": "You are a librarian with expertise in book recommendations. Suggest highly-rated books that match the user's interests."},
        {"role": "user", "content": "Recommend me a science fiction book"}
    ],
    response_format=BookRecommendation
)

print(response.choices[0].message.parsed)
# Output: title='Dune' author='Frank Herbert' genre='Science Fiction' reading_time_minutes=2070



client.chat.completions.create(
    model="openai/gpt-6-luna",
    messages=[...],
    extra_body={"reasoning": {"effort": "high"}},  # low / medium / high / minimal / xhigh
    max_tokens=1000,  # Cap total output tokens
)