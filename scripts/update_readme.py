"""Rewrites the "Recently shipped" block of README.md with my latest public commits.

Runs daily from .github/workflows/update-readme.yml. Standard library only.
"""
import json
import os
import re
import urllib.request
from pathlib import Path

USER = "Milan32555"
SKIP = {USER}  # the profile repo itself
LIMIT = 5
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- recent starts -->", "<!-- recent ends -->"
# Housekeeping commits say little about the work itself; prefer the latest real change.
NOISE = re.compile(r"^(docs|chore|style|ci|build|test)(\(.*?\))?!?:", re.I)
# Shorter labels for repos with very long names.
DISPLAY = {
    "Full-stack-library-management-system-with-Vue.js-frontend-and-Node.js-backend": "library-system",
    "AnimalVision-AI-Image-Classification-System": "AnimalVision",
}


def get(url: str):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": USER}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return json.load(r)


def clean(message: str) -> str:
    first = message.splitlines()[0].strip()
    return first.replace("<", "&lt;").replace(">", "&gt;").replace("|", r"\|")


def entries() -> list[str]:
    repos = get(f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30")
    repos = [r for r in repos if not r["fork"] and not r["archived"] and r["name"] not in SKIP][:LIMIT]
    lines = []
    for repo in repos:
        commits = get(f"https://api.github.com/repos/{USER}/{repo['name']}/commits?per_page=30")
        commit = next((c for c in commits if not NOISE.match(c["commit"]["message"])), commits[0])
        date = commit["commit"]["committer"]["date"][:10]
        name = DISPLAY.get(repo["name"], repo["name"])
        lines.append(f"- **[{name}]({repo['html_url']})** — {clean(commit['commit']['message'])} <sub>{date}</sub>")
    return lines


def main() -> None:
    text = README.read_text(encoding="utf-8")
    block = "\n".join([START, *entries(), END])
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), block, text, flags=re.S)
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print("README updated")
    else:
        print("No changes")


if __name__ == "__main__":
    main()
