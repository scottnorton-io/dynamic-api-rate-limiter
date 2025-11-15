"""Example: Using the dynamic rate limiter with the OpenAI API.

This example uses the HTTP client directly (no official SDK) and shows how
to send a simple chat completion request.

Requirements:

- Set OPENAI_API_KEY to your API key.
- Optionally set OPENAI_MODEL to override the default model name.
"""

import os

from api_ratelimiter import make_client_for


def main() -> None:
    client = make_client_for("openai")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("Please set OPENAI_API_KEY environment variable.")

    model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": "Say hello from dynamic-api-rate-limiter."}
        ],
    }

    resp = client.request("POST", "/chat/completions", headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    print("OpenAI response:", data)


if __name__ == "__main__":
    main()
