import os
from openai import OpenAI

def get_client(API_provider) -> OpenAI:
    """
    Returns an OpenAI client instance.
    """
    if API_provider == "OpenRouter":
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.environ["OPENROUTER_API_KEY"]
        )
    elif API_provider == "OpenAI":
        client = OpenAI(
            base_url="https://api.openai.com/v1",
            api_key=os.environ["OPENAI_API_KEY"]
        )
        for m in sorted(client.models.list(), key=lambda m: m.id):
            print(m.id)
    else:
        raise ValueError(f"Unsupported API provider: {API_provider}")
    return client