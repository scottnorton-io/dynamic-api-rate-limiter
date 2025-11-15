"""
Minimal Fieldguide usage example.

Set FIELDGUIDE_TOKEN before running this script.

The endpoint used here is illustrative; adjust path/fields to match your account and API version.
"""

import os

from api_ratelimiter.clients import make_client_for


def list_engagements(token: str):
    fg = make_client_for("fieldguide")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    resp = fg.request("GET", "/v1/engagements", headers=headers)
    resp.raise_for_status()
    return resp.json()


def main():
    token = os.environ.get("FIELDGUIDE_TOKEN", "").strip()
    if not token:
        raise SystemExit("Please set FIELDGUIDE_TOKEN environment variable.")

    data = list_engagements(token)
    print("Engagements response keys:", list(data.keys()))


if __name__ == "__main__":
    main()
