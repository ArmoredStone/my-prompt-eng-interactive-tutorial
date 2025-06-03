import os
import anthropic
import re

def get_completion(client, model_name: str, prompt: str, assistant: str = "", temperature: float = 0.0):
    response = client.messages.create(
        model=model_name,
        max_tokens=2000,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}, {"role": "assistant", "content": assistant}],
    )
    return response.content[0].text

# Function to grade exercise correctness
def grade_exercise_1(text):
    return "hola" in text.lower()

def grade_exercise_2(text):
    return text == "Michael Jordan"

def grade_exercise_3(text):
    trimmed = text.strip()
    words = len(trimmed.split())
    return words >= 800

def main():
    API_KEY = os.getenv("API_KEY")
    client = anthropic.Anthropic(api_key=API_KEY)
    MODEL_NAME = "claude-sonnet-4-20250514"

    # PROMPT = "Write a haiku about robots."
    # SYSTEM_PROMPT = ""
    # completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    # print(completion)
    # print("-" * 30)

    # PROMPT = "Write a haiku about robots. No preamble, just the haiku."
    # SYSTEM_PROMPT = ""
    # completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    # print(completion)
    # print("-" * 30)
    
    # PROMPT = "Write a haiku about robots."
    # SYSTEM_PROMPT = "No preamble, just the haiku."
    # completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    # print(completion)
    # print("-" * 30)

    # PROMPT = "Who is the best basketball player of all time?"
    # SYSTEM_PROMPT = ""
    # completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    # print(completion)
    # print("-" * 30)

    PROMPT = "Hello Claude, how are you?"
    SYSTEM_PROMPT = "Answer in Spanish language"
    completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    print(completion)
    print(grade_exercise_1(completion))
    print("-" * 30)

    PROMPT = "Who is the best basketball player of all time? Answer single best player name, remove special symbols and numbers"
    SYSTEM_PROMPT = ""
    completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    print(completion)
    print(grade_exercise_2(completion))
    print("-" * 30)

    PROMPT = "Write an adventure story"
    SYSTEM_PROMPT = "at least 800 words in length, remove preamble"
    completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    print(completion)
    print(grade_exercise_3(completion))
    print("-" * 30)

if __name__ == "__main__":
    main()