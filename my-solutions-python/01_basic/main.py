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

def grade_exercise_1(text: str):
    pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
    return bool(pattern.match(text))

def grade_exercise_2(text: str):
    return bool(re.search(r"giggles", text) or re.search(r"soo", text))

def main():
    API_KEY = os.getenv("API_KEY")
    client = anthropic.Anthropic(api_key=API_KEY)
    MODEL_NAME = "claude-sonnet-4-20250514"


    # Exercise 1
    PROMPT = "Count to 3"
    SYSTEM_PROMPT = ""
    completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    print(grade_exercise_1(completion))
    print(completion)

    print("-" * 30)

    # Exercise 2
    PROMPT = "How big is the sky?"
    SYSTEM_PROMPT = "You are a 3 year old child don't forget to soo or giggle in the answer"
    completion = get_completion(client, MODEL_NAME, PROMPT, SYSTEM_PROMPT, temperature=0.0)
    print(grade_exercise_2(completion))
    print(completion)


    print("-" * 30)
    # example playground
    PROMPT = "Hi Claude, how are you?"
    print(get_completion(client, MODEL_NAME, PROMPT, temperature=0.0))
    print("-" * 30)

    PROMPT = "Can you tell me the color of the ocean?"
    print(get_completion(client, MODEL_NAME, PROMPT, temperature=0.0))
    print("-" * 30)

    PROMPT = "What year was Celine Dion born in?"
    print(get_completion(client, MODEL_NAME, PROMPT, temperature=0.0))
    print("-" * 30)
    
    PROMPT = "Why is the sky blue?"
    SYSTEM_PROMPT = "Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question."
    print(get_completion(client, MODEL_NAME, PROMPT, temperature=0.0))
    print("-" * 30)

if __name__ == "__main__":
    main()