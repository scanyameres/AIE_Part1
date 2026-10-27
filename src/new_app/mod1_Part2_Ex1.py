import os
from urllib import response
from xmlrpc import client
from openai import OpenAI
from new_app.config import get_client

if __name__ == "__main__":

    question = "What is a dog?"
    print("Part 1:" + question)
    client = get_client("OpenRouter")
    response = client.chat.completions.create(
        model="openai/gpt-6-luna",
        messages=[
            {"role": "user", "content": question},
            #{"role": "system", "content": "You are an AI research assistant. You use a tone that is technical and scientific."},
            #{"role": "user", "content": "Hello, who are you?"},
            #{"role": "assistant", "content": "Greeting! I am an AI research assistant. How can I help you today?"},
            #{"role": "user", "content": "Can you tell me about the creation of black holes?"}
            #temperature=1.99,
        ],
    )
    print(response.choices[0].message.content)   


    print("Part 2: Give content and answer a question from the context.")

    CONTENT = """Answer the question based on the context below. Keep the answer short and concise. Respond \"Unsure about answer\" if not sure about the answer.
    Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.
    Question: What was OKT3 originally sourced from?
    """

    response = client.chat.completions.create(
        model="openai/gpt-6-luna",
        messages=[
            {"role": "user", "content": CONTENT},
        ],
        temperature=0,
    )

    #IPython.display.Markdown(response.choices[0].message.content)
    print(response.choices[0].message.content)