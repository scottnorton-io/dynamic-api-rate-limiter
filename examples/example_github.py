"""Example: Using the dynamic rate limiter with the GitHub REST API.

This example assumes you have:

- A GitHub personal access token in GITHUB_TOKEN
- Optionally, an organization name in GITHUB_ORG (otherwise your user is used)

It lists repositories for the authenticated user or organization.
"""

import os

from api_ratelimiter import make_client_for


def main() -> None:
    client = make_client_for("github")

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("Please set GITHUB_TOKEN environment variable.")

    org = os.environ.get("GITHUB_ORG")
    if org:
        path = f"/orgs/{org}/repos"
    else:
        path = "/user/repos"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }

    resp = client.request("GET", path, headers=headers)
    resp.raise_for_status()
    repos = resp.json()

    print("Repositories:")
    for repo in repos:
        print("-", repo.get("full_name"))


if __name__ == "__main__":
    main()
