import os
import anthropic

def get_completion(client, model_name: str, prompt: str, temperature: float = 0.0):
    response = client.messages.create(
        model=model_name,
        max_tokens=2000,
        temperature=temperature,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text

def main():
    API_KEY = os.getenv("API_KEY")
    client = anthropic.Anthropic(api_key=API_KEY)
    MODEL_NAME = "claude-sonnet-4-20250514"

    #
    #
    #

    prompt = "Hello, Claude!"

    #
    #
    #

    completion = get_completion(client, MODEL_NAME, prompt, temperature=0.0)
    print(completion)

if __name__ == "__main__":
    main()