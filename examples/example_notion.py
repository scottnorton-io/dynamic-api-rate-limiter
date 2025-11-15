"""
Minimal Notion usage example.

Set NOTION_TOKEN and PAGE_ID before running this script.

This example is intentionally simple and does not handle all Notion features.
"""

import os

from api_ratelimiter.clients import make_client_for


def get_page(page_id: str, token: str):
    notion = make_client_for("notion")

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
    }

    resp = notion.request("GET", f"/pages/{page_id}", headers=headers)
    resp.raise_for_status()
    return resp.json()


def main():
    token = os.environ.get("NOTION_TOKEN", "").strip()
    page_id = os.environ.get("NOTION_PAGE_ID", "").strip()

    if not token or not page_id:
        raise SystemExit(
            "Please set NOTION_TOKEN and NOTION_PAGE_ID environment variables."
        )

    data = get_page(page_id, token)
    print("Page ID:", data.get("id"))
    print("Archived:", data.get("archived"))


if __name__ == "__main__":
    main()
