"""Example: Using the dynamic rate limiter with the Vanta API.

NOTE: This is a placeholder example. Adjust the base URL and endpoint
to match your actual Vanta API usage and authentication model.
"""

import os

from api_ratelimiter.clients import make_client_for


def main() -> None:
    token = os.environ.get("VANTA_TOKEN")

    if not token:
        raise SystemExit("Please set VANTA_TOKEN environment variable.")

    vanta = make_client_for("vanta")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Replace `/some-endpoint` with a real Vanta API path you use regularly.
    resp = vanta.request("GET", "/some-endpoint", headers=headers)
    resp.raise_for_status()
    data = resp.json()

    print("Fetched Vanta data:")
    print(data)


if __name__ == "__main__":
    main()
