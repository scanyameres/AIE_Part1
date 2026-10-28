from openai import OpenAI
from new_app.config import get_client

client = get_client("OpenRouter")
MODEL = "openai/gpt-6-luna"

# The instructions parameter gives the model high-level instructions on how it should behave
# while generating a response, including tone, goals, and examples of correct responses.
# Any instructions provided this way will take priority over a prompt in the input parameter.

response = client.responses.create(
    model=MODEL,
    reasoning={"effort": "low"},
    instructions="Talk like a pirate.",
    input="Are semicolons optional in JavaScript?",
)

print(response.output_text)

# The example above is roughly equivalent to using the following input messages in the input array:

response = client.responses.create(
    model=MODEL,
    reasoning={"effort": "low"},
    input=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)

#For new prompt-engineering work:
#Keep prompt builders in a small module near the feature they support.
#Use typed function arguments or schemas for dynamic values such as customer data, files, or task options.
#Pass the generated instructions and input directly to the Responses API.
#Add representative fixtures, tests, and evaluation checks before changing production prompts.
#Roll out prompt changes through your deployment system, using feature flags or configuration when you need staged releases.
