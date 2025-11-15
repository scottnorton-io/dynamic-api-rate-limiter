"""Example: Using the dynamic rate limiter with the Notion API."""

import os

from api_ratelimiter.clients import make_client_for


def main() -> None:
    token = os.environ.get("NOTION_TOKEN")
    page_id = os.environ.get("NOTION_PAGE_ID")

    if not token or not page_id:
        raise SystemExit(
            "Please set NOTION_TOKEN and NOTION_PAGE_ID environment variables."
        )

    notion = make_client_for("notion")

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
    }

    resp = notion.request("GET", f"/pages/{page_id}", headers=headers)
    resp.raise_for_status()
    data = resp.json()

    print("Fetched Notion page:")
    print(data)


if __name__ == "__main__":
    main()
