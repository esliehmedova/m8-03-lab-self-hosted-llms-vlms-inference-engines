from openai import OpenAI

# Point the OpenAI client at your LOCAL Ollama server instead of the cloud.
# This is the whole insight of the lab: "calling an LLM" is just an HTTP
# request to an inference server — wherever that server happens to run.
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # required by the client, but ignored by Ollama
)

MODEL = "llama3.2:3b"


def main() -> None:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a concise assistant."},
            {"role": "user", "content": "In one sentence, what is an inference engine?"},
        ],
    )
    print(response.choices[0].message.content)
    print("\n--- Reflection ---")
    print(
        "This is the same shape as yesterday's hosted Gemini call because both are "
        "just HTTP POST requests to an OpenAI-style /chat/completions endpoint, with "
        "a model name and a messages list, returning a JSON response with the same "
        "structure. The client code, request format, and response parsing are "
        "identical; the only thing that changed is the base_url — pointing at "
        "localhost:11434 (my own machine) instead of a cloud provider's server. "
        "This proves that 'calling an LLM' is fundamentally just talking to an "
        "inference server over HTTP, regardless of whether that server is in a "
        "data center or running on my laptop."
    )


if __name__ == "__main__":
    main() 