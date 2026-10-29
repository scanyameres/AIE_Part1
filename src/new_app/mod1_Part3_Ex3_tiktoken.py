from pydantic import BaseModel
from openai import OpenAI
from new_app.config import get_client
import tiktoken

client = get_client("OpenRouter")

# Define the prompt you want tokenized
text = f"""
France, Paris.
Paris, France
"""
#Paris, Paris, Paris France, Eiffel Tower, Louvre, Seine, Montmartre, Paris, Notre Dame, Paris, Sacré-Cœur, Champs-Élysées, Arc de Triomphe, Tuileries Garden, Luxembourg Gardens, Orsay Museum, Pompidou Center, Latin Quarter, Marais District, Bastille, Place de la Concorde, Palais Garnier, Opéra Bastille, Palais Royal, Place Vendôme.

# Tokenizer demonstration uses Mini; the completion helper below uses Luna.
encoding = tiktoken.encoding_for_model("gpt-5.4-mini")

# Encode the text - gives you the tokens in integer form
tokens = encoding.encode(text)
print(tokens);

# Decode the integers to see what the text versions look like
[encoding.decode_single_token_bytes(token) for token in tokens]

## Updated
def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="openai/gpt-6-luna",
        max_tokens=800,
        messages=messages
    )
    return response.choices[0].message.content

## ---------- Call the helper method

### 1. Set primary content or prompt text
text = f"""
If you're happy and you know it
"""

### 2. Use that in the prompt template below
prompt = f"""
```{text}```
"""

## 3. Run the prompt
response = get_completion(prompt)
print(response)



# Test Example
# https://platform.openai.com/playground/p/default-summarize

## Example text
text = f"""
Jupiter is the fifth planet from the Sun and the \
largest in the Solar System. It is a gas giant with \
a mass one-thousandth that of the Sun, but two-and-a-half \
times that of all the other planets in the Solar System combined. \
Jupiter is one of the brightest objects visible to the naked eye \
in the night sky, and has been known to ancient civilizations since \
before recorded history. It is named after the Roman god Jupiter.[19] \
When viewed from Earth, Jupiter can be bright enough for its reflected \
light to cast visible shadows,[20] and is on average the third-brightest \
natural object in the night sky after the Moon and Venus.
"""

## Set the prompt
prompt = f"""
Summarize content you are provided with for a second-grade student.
```{text}```
"""

## Run the prompt
response = get_completion(prompt)
print(response)



###### Select techniques for Prompt optimization and execute them


# Demonstration of 2-3 Prompt Optimization Techniques
# We will use 'Least-to-Most Prompting' and 'Self-Refinement'

print("=== Technique 1: Least-to-Most Prompting ===\n")

# Step 1: Deconstruct a complex math/logic problem into simpler steps
subproblem_prompt_1 = """
Problem: Elspeth is twice as old as her brother Liam. In 5 years, Liam will be 15. How old is Elspeth now?

Let's break this down into smaller subproblems:
Subproblem 1: How old is Liam in 5 years?
Subproblem 2: How old is Liam now?
Subproblem 3: How old is Elspeth now based on Liam's current age?

Let's solve Subproblem 1 and Subproblem 2 first.
"""

response_1 = client.chat.completions.create(
    model="openai/gpt-6-luna",
    max_tokens=300,
    messages=[{"role": "user", "content": subproblem_prompt_1}]
)
sol_step_1 = response_1.choices[0].message.content
print("Step 1 Output:\n", sol_step_1)

# Step 2: Use the previous solution to solve the main problem
subproblem_prompt_2 = f"""
Problem: Elspeth is twice as old as her brother Liam. In 5 years, Liam will be 15. How old is Elspeth now?

We know from the previous steps:
{sol_step_1}

Now, solve the final subproblem: How old is Elspeth now?
"""

response_2 = client.chat.completions.create(
    model="openai/gpt-6-luna",
    max_tokens=300,
    messages=[{"role": "user", "content": subproblem_prompt_2}]
)
print("\nStep 2 Output (Final Solution):\n", response_2.choices[0].message.content)


print("\n=== Technique 2: Self-Refinement ===\n")

# Step 1: Generate initial draft
initial_prompt = "Write a short 3-sentence description of quantum computing for a 10-year-old."
initial_response = client.chat.completions.create(
    model="openai/gpt-6-luna",
    max_tokens=200,
    messages=[{"role": "user", "content": initial_prompt}]
)
draft = initial_response.choices[0].message.content
print("Draft:\n", draft)

# Step 2: Self-critique and refine the response
refinement_prompt = f"""
Here is an initial explanation of quantum computing for a 10-year-old:
\"{draft}\"

Critique this explanation to ensure it is extremely simple, has exactly 3 sentences, and uses an analogy. Then, output the refined explanation.
"""

refined_response = client.chat.completions.create(
    model="openai/gpt-6-luna",
    max_tokens=1350,
    messages=[{"role": "user", "content": refinement_prompt}]
)
print("\nRefined Output:\n", refined_response.choices[0].message.content)
print(refined_response.choices[0].finish_reason)  # "length" means it ran out of tokens
print(refined_response.usage)                     # look at completion_tokens_details.reasoning_tokens
