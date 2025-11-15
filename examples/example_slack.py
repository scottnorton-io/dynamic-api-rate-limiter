"""Example: Using the dynamic rate limiter with the Slack Web API.

This example assumes you have:

- A Slack bot/user token in SLACK_BOT_TOKEN
- A channel ID in SLACK_CHANNEL_ID

It posts a simple message to the channel using chat.postMessage.
"""

import os

from api_ratelimiter import make_client_for


def main() -> None:
    client = make_client_for("slack")

    token = os.environ.get("SLACK_BOT_TOKEN")
    channel = os.environ.get("SLACK_CHANNEL_ID")
    if not token or not channel:
        raise SystemExit(
            "Please set SLACK_BOT_TOKEN and SLACK_CHANNEL_ID environment variables."
        )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8",
    }
    payload = {
        "channel": channel,
        "text": "Hello from dynamic-api-rate-limiter + Slack!",
    }

    resp = client.request("POST", "/chat.postMessage", headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    print("Slack response:", data)


if __name__ == "__main__":
    main()
