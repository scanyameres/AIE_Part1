import os

from openai import OpenAI

def main() -> None:
    print("Hello from new-app!")
    print("What is the meaning of life?")
    print("Thinking...")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"]
    )

    response = client.chat.completions.create(
        model="openai/gpt-6-luna",
        messages=[
            {"role": "user", "content": "What is the meaning of life?"},
        ],
    )

    print(response.choices[0].message.content)
    print("Goodbye!")

if __name__ == "__main__":
    main()

