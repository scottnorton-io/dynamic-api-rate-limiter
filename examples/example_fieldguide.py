"""Example: Using the dynamic rate limiter with the Fieldguide API.

NOTE: This is a placeholder example. Adjust the base URL, endpoint,
and authentication headers to match your actual Fieldguide usage.
"""

import os

from api_ratelimiter.clients import make_client_for


def main() -> None:
    token = os.environ.get("FIELDGUIDE_TOKEN")

    if not token:
        raise SystemExit("Please set FIELDGUIDE_TOKEN environment variable.")

    fg = make_client_for("fieldguide")

    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Replace `/some-endpoint` with a real Fieldguide API path you use regularly.
    resp = fg.request("GET", "/some-endpoint", headers=headers)
    resp.raise_for_status()
    data = resp.json()

    print("Fetched Fieldguide data:")
    print(data)


if __name__ == "__main__":
    main()
