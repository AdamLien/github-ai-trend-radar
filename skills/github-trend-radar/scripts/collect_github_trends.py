#!/usr/bin/env python3
"""Collect GitHub repo metrics and write a trend radar report."""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import json
import os
import sqlite3
import sys
import textwrap
from html.parser import HTMLParser
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_ROOT = "https://api.github.com"
TRENDING_DAILY_URL = "https://github.com/trending?since=daily"
SCOPE_KEYWORDS = (
    "ai", "agent", "automation", "claude", "codex", "coding", "cursor", "developer",
    "knowledge", "llm", "mcp", "model context protocol", "orchestrat", "rag", "skill", "wiki",
)
PINNED_WATCHLIST = ("stablyai/orca",)


class TrendingDailyParser(HTMLParser):
    """Extract repository links, descriptions, and daily stars from Trending cards."""

    def __init__(self) -> None:
        super().__init__()
        self.cards: list[dict[str, str]] = []
        self.card: dict[str, str] | None = None
        self.depth = 0
        self.heading_depth: int | None = None
        self.capture_description = False
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "article" and "Box-row" in (attributes.get("class") or ""):
            self.card = {"repo": "", "description": "", "stars_today": "0"}
            self.depth = 1
            return
        if not self.card:
            return
        self.depth += 1
        if tag == "h2":
            self.heading_depth = self.depth
        if tag == "a" and self.heading_depth is not None and not self.card["repo"]:
            href = attributes.get("href") or ""
            if href.count("/") == 2 and href.startswith("/"):
                self.card["repo"] = href.strip("/")
        if tag == "p":
            self.capture_description = True
            self.text = []

    def handle_data(self, data: str) -> None:
        if not self.card:
            return
        if self.capture_description:
            self.text.append(data)
        match = re.search(r"([0-9,]+)\s+stars today", data)
        if match:
            self.card["stars_today"] = match.group(1).replace(",", "")

    def handle_endtag(self, tag: str) -> None:
        if not self.card:
            return
        if tag == "p" and self.capture_description:
            self.card["description"] = " ".join(" ".join(self.text).split())
            self.capture_description = False
        if tag == "h2":
            self.heading_depth = None
        self.depth -= 1
        if tag == "article" and self.depth == 0:
            self.cards.append(self.card)
            self.card = None


def is_in_scope(repo: str, description: str) -> bool:
    text = f"{repo} {description}".lower()
    return any(keyword in text for keyword in SCOPE_KEYWORDS)


def parse_trending_daily(html: str) -> dict[str, dict[str, int]]:
    parser = TrendingDailyParser()
    parser.feed(html)
    return {
        card["repo"]: {"trending_stars_today": int(card["stars_today"])}
        for card in parser.cards
        if card["repo"] and is_in_scope(card["repo"], card["description"])
    }


def fetch_trending_daily() -> dict[str, dict[str, int]]:
    request = urllib.request.Request(TRENDING_DAILY_URL, headers={"User-Agent": "github-trend-radar"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return parse_trending_daily(response.read().decode("utf-8", errors="replace"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"GitHub Trending request failed: {exc}") from exc


def merge_sources(
    search_repos: list[str],
    trending_repos: dict[str, dict[str, int]],
    pinned_repos: list[str] | tuple[str, ...] = (),
) -> dict[str, list[str]]:
    sources = {repo: ["search"] for repo in search_repos}
    for repo in trending_repos:
        sources.setdefault(repo, []).append("trending_daily")
    for repo in pinned_repos:
        sources.setdefault(repo, []).append("pinned_watchlist")
    return sources


def github_get(path: str, token: str | None) -> Any:
    url = path if path.startswith("https://") else f"{API_ROOT}{path}"
    request = urllib.request.Request(url)
    request.add_header("Accept", "application/vnd.github+json")
    request.add_header("X-GitHub-Api-Version", "2022-11-28")
    request.add_header("User-Agent", "github-trend-radar")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API {exc.code} for {url}: {body[:500]}") from exc


def read_lines(path: str | None) -> list[str]:
    if not path:
        return []
    items: list[str] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        clean = line.strip()
        if clean and not clean.startswith("#"):
            items.append(clean)
    return items


def normalize_repo(value: str) -> str:
    clean = value.strip()
    if clean.startswith("https://github.com/"):
        clean = clean.removeprefix("https://github.com/")
    clean = clean.strip("/")
    parts = clean.split("/")
    if len(parts) < 2:
        raise ValueError(f"Repo must be owner/name or GitHub URL: {value}")
    return f"{parts[0]}/{parts[1]}"


def repo_record(full_name: str, token: str | None, include_readme: bool) -> dict[str, Any]:
    data = github_get(f"/repos/{full_name}", token)
    latest_release = None
    try:
        latest_release = github_get(f"/repos/{full_name}/releases/latest", token)
    except RuntimeError:
        latest_release = None

    readme_excerpt = ""
    if include_readme:
        try:
            readme = github_get(f"/repos/{full_name}/readme", token)
            content = base64.b64decode(readme.get("content", "")).decode("utf-8", errors="replace")
            readme_excerpt = " ".join(content.split())[:700]
        except Exception:
            readme_excerpt = ""

    return {
        "full_name": data["full_name"],
        "html_url": data["html_url"],
        "description": data.get("description") or "",
        "language": data.get("language") or "",
        "license": (data.get("license") or {}).get("spdx_id") or "",
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "open_issues": data.get("open_issues_count", 0),
        "watchers": data.get("subscribers_count", 0),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
        "pushed_at": data.get("pushed_at"),
        "archived": data.get("archived", False),
        "disabled": data.get("disabled", False),
        "topics": data.get("topics", []),
        "latest_release": {
            "name": latest_release.get("name") if latest_release else "",
            "tag_name": latest_release.get("tag_name") if latest_release else "",
            "published_at": latest_release.get("published_at") if latest_release else "",
        },
        "readme_excerpt": readme_excerpt,
    }


def search_repos(query: str, token: str | None, limit: int) -> list[str]:
    params = urllib.parse.urlencode({"q": query, "sort": "stars", "order": "desc", "per_page": limit})
    data = github_get(f"/search/repositories?{params}", token)
    return [item["full_name"] for item in data.get("items", [])]


def load_previous_snapshot(snapshot_dir: Path) -> dict[str, dict[str, Any]]:
    if not snapshot_dir.exists():
        return {}
    snapshots = sorted(snapshot_dir.glob("repos-*.json"))
    if not snapshots:
        return {}
    previous = json.loads(snapshots[-1].read_text(encoding="utf-8"))
    return {item["full_name"]: item for item in previous.get("repos", [])}


def load_previous_daily_snapshot(out_dir: Path) -> dict[str, dict[str, Any]]:
    """Use the preceding target-date folder, not a rerun's own execution snapshot."""
    daily_dir = out_dir.parent
    previous_dirs = sorted(path for path in daily_dir.iterdir() if path.is_dir() and path.name < out_dir.name)
    if not previous_dirs:
        return {}
    previous_path = previous_dirs[-1] / "repos.json"
    if not previous_path.exists():
        return {}
    payload = json.loads(previous_path.read_text(encoding="utf-8"))
    return {item["full_name"]: item for item in payload.get("repos", [])}


def load_tracked_repo_names(out_dir: Path) -> set[str]:
    """Return the union of every prior daily candidate set for a cumulative radar."""
    tracked: set[str] = set()
    for folder in out_dir.parent.iterdir():
        if not folder.is_dir() or folder.name > out_dir.name:
            continue
        payload_path = folder / "repos.json"
        if not payload_path.exists():
            continue
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
        tracked.update(record["full_name"] for record in payload.get("repos", []))
    return tracked


def load_tracked_records(out_dir: Path) -> dict[str, dict[str, Any]]:
    """Keep the most recently captured metadata for every historically discovered repo."""
    records: dict[str, dict[str, Any]] = {}
    for folder in sorted(path for path in out_dir.parent.iterdir() if path.is_dir() and path.name <= out_dir.name):
        payload_path = folder / "repos.json"
        if not payload_path.exists():
            continue
        payload = json.loads(payload_path.read_text(encoding="utf-8"))
        records.update({record["full_name"]: record for record in payload.get("repos", [])})
    return records


def add_deltas(records: list[dict[str, Any]], previous: dict[str, dict[str, Any]]) -> None:
    for record in records:
        old = previous.get(record["full_name"], {})
        record["stars_delta"] = record["stars"] - int(old.get("stars", record["stars"]))
        record["forks_delta"] = record["forks"] - int(old.get("forks", record["forks"]))
        record["previous_snapshot"] = old.get("snapshot_date", "")
        record["is_new"] = record["full_name"] not in previous


def mark_new_entries(records: list[dict[str, Any]], historical_names: set[str], current_discoveries: set[str]) -> None:
    """A new entry must be discovered today and absent from all previous target dates."""
    for record in records:
        record["is_new"] = record["full_name"] in current_discoveries and record["full_name"] not in historical_names
    """A new entry must be discovered today and absent from all previous target dates."""
    for record in records:
        record["is_new"] = record["full_name"] in current_discoveries and record["full_name"] not in historical_names


def classify(record: dict[str, Any]) -> str:
    if record.get("archived") or record.get("disabled"):
        return "Reference only"
    if record.get("stars_delta", 0) >= 50:
        return "Deep research"
    if record.get("stars_delta", 0) >= 10:
        return "Demo candidate"
    if any(topic in {"mcp", "llm", "ai-agent", "rag"} for topic in record.get("topics", [])):
        return "Watch"
    return "Reference only"


def init_db(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS repos (
            full_name TEXT PRIMARY KEY,
            html_url TEXT NOT NULL,
            description TEXT,
            language TEXT,
            license TEXT,
            created_at TEXT,
            archived INTEGER DEFAULT 0,
            disabled INTEGER DEFAULT 0,
            topics_json TEXT,
            first_seen_at TEXT NOT NULL,
            last_seen_at TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS repo_snapshots (
            full_name TEXT NOT NULL,
            snapshot_date TEXT NOT NULL,
            stars INTEGER NOT NULL,
            forks INTEGER NOT NULL,
            open_issues INTEGER NOT NULL,
            watchers INTEGER NOT NULL,
            updated_at TEXT,
            pushed_at TEXT,
            latest_release_json TEXT,
            readme_excerpt TEXT,
            category TEXT,
            PRIMARY KEY (full_name, snapshot_date)
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS search_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_date TEXT NOT NULL,
            query TEXT NOT NULL,
            repo_full_name TEXT NOT NULL,
            rank INTEGER NOT NULL
        )
        """
    )
    return conn


def write_db(conn: sqlite3.Connection, records: list[dict[str, Any]], queries: list[str], discovered_by_query: dict[str, list[str]], date: str) -> None:
    for record in records:
        conn.execute(
            """
            INSERT INTO repos (
                full_name, html_url, description, language, license, created_at,
                archived, disabled, topics_json, first_seen_at, last_seen_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(full_name) DO UPDATE SET
                html_url=excluded.html_url,
                description=excluded.description,
                language=excluded.language,
                license=excluded.license,
                archived=excluded.archived,
                disabled=excluded.disabled,
                topics_json=excluded.topics_json,
                last_seen_at=excluded.last_seen_at
            """,
            (
                record["full_name"],
                record["html_url"],
                record["description"],
                record["language"],
                record["license"],
                record["created_at"],
                int(record["archived"]),
                int(record["disabled"]),
                json.dumps(record.get("topics", []), ensure_ascii=False),
                date,
                date,
            ),
        )
        conn.execute(
            """
            INSERT INTO repo_snapshots (
                full_name, snapshot_date, stars, forks, open_issues, watchers,
                updated_at, pushed_at, latest_release_json, readme_excerpt, category
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(full_name, snapshot_date) DO UPDATE SET
                stars=excluded.stars,
                forks=excluded.forks,
                open_issues=excluded.open_issues,
                watchers=excluded.watchers,
                updated_at=excluded.updated_at,
                pushed_at=excluded.pushed_at,
                latest_release_json=excluded.latest_release_json,
                readme_excerpt=excluded.readme_excerpt,
                category=excluded.category
            """,
            (
                record["full_name"],
                date,
                record["stars"],
                record["forks"],
                record["open_issues"],
                record["watchers"],
                record["updated_at"],
                record["pushed_at"],
                json.dumps(record.get("latest_release", {}), ensure_ascii=False),
                record.get("readme_excerpt", ""),
                record.get("category", ""),
            ),
        )
    for query in queries:
        for rank, repo in enumerate(discovered_by_query.get(query, []), start=1):
            conn.execute(
                "INSERT INTO search_runs (run_date, query, repo_full_name, rank) VALUES (?, ?, ?, ?)",
                (date, query, repo, rank),
            )
    conn.commit()


def markdown_report(records: list[dict[str, Any]], queries: list[str], repos: list[str], date: str) -> str:
    sorted_records = sorted(records, key=lambda row: (row.get("stars_delta", 0), row.get("stars", 0)), reverse=True)
    new_entries = [row for row in records if row.get("is_new")]
    lines = [
        f"# GitHub Trend Radar - {date}",
        "",
        "## Executive Summary",
        "",
        f"- Repositories checked: {len(records)}",
        f"- New in-scope Trending entries: {len(new_entries)}",
        f"- Search queries: {', '.join(queries) if queries else 'none'}",
        f"- Seed repos: {', '.join(repos) if repos else 'none'}",
        "",
        "## Top Movers",
        "",
        "| Repo | Stars | Snapshot delta | Trending today | Forks | Updated | Category | Why it matters |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for record in sorted_records[:20]:
        why = record["description"].replace("|", "/")[:110] or "No description"
        lines.append(
            f"| [{record['full_name']}]({record['html_url']}) | {record['stars']} | "
            f"{'new' if record.get('is_new') else record.get('stars_delta', 0)} | "
            f"{record.get('trending_stars_today') or '—'} | {record['forks']} | "
            f"{(record.get('pushed_at') or '')[:10]} | {record['category']} | {why} |"
        )

    lines.extend(["", "## New Trending Entries", ""])
    if new_entries:
        for record in sorted(new_entries, key=lambda row: row.get("trending_stars_today") or 0, reverse=True):
            lines.append(
                f"- [{record['full_name']}]({record['html_url']}): "
                f"{record.get('trending_stars_today', 0)} stars today; first observed in this radar, so snapshot growth is unmeasured."
            )
    else:
        lines.append("- No in-scope Trending entries were new to this radar.")

    lines.extend(["", "## Deep Research Candidates", ""])
    deep = [row for row in sorted_records if row["category"] == "Deep research"]
    if deep:
        for record in deep[:10]:
            lines.append(f"- [{record['full_name']}]({record['html_url']}): {record['description']}")
    else:
        lines.append("- No deep research candidates crossed the default momentum threshold in this run.")

    lines.extend(["", "## Demo And Content Ideas", ""])
    for record in sorted_records[:8]:
        lines.append(
            f"- Compare or demo `{record['full_name']}` around: "
            f"{record['description'] or 'its core workflow and adoption tradeoffs'}."
        )

    lines.extend(["", "## Risks And False Positives", ""])
    risky = [row for row in sorted_records if row.get("archived") or not row.get("license")]
    if risky:
        for record in risky[:8]:
            reason = "archived" if record.get("archived") else "license unclear"
            lines.append(f"- `{record['full_name']}`: {reason}.")
    else:
        lines.append("- No obvious archive/license risks in the top collected records.")

    lines.extend(["", "## Next Run", "", "- Re-run with the same `--out` directory to calculate star deltas from saved snapshots."])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", action="append", default=[], help="Repository as owner/name or GitHub URL.")
    parser.add_argument("--repos-file", help="Text file with one repo per line.")
    parser.add_argument("--query", action="append", default=[], help="GitHub repository search query.")
    parser.add_argument("--queries-file", help="Text file with one search query per line.")
    parser.add_argument("--limit", type=int, default=10, help="Max repos per query.")
    parser.add_argument("--include-trending-daily", action="store_true", help="Merge in-scope GitHub Trending daily repos.")
    parser.add_argument("--out", default="outputs/github-radar", help="Output directory.")
    parser.add_argument("--db", help="Optional SQLite database path.")
    parser.add_argument("--include-readme", action="store_true", help="Include short README excerpts.")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    date = dt.date.today().isoformat()
    out_dir = Path(args.out)
    snapshot_dir = out_dir / "snapshots"
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    seed_repos = [normalize_repo(repo) for repo in args.repo + read_lines(args.repos_file)]
    queries = args.query + read_lines(args.queries_file)

    discovered: list[str] = []
    discovered_by_query: dict[str, list[str]] = {}
    for query in queries:
        query_repos = search_repos(query, token, args.limit)
        discovered_by_query[query] = query_repos
        discovered.extend(query_repos)

    trending_repos = fetch_trending_daily() if args.include_trending_daily else {}
    sources = merge_sources(seed_repos + discovered, trending_repos, PINNED_WATCHLIST)
    historical_records = load_tracked_records(out_dir)
    tracked_records = historical_records
    tracked_names = set(tracked_records)
    for repo in tracked_names:
        sources.setdefault(repo, ["tracked"])
    repo_names = sorted(sources)
    if not repo_names:
        print("No repositories or queries provided.", file=sys.stderr)
        return 2

    previous = load_previous_daily_snapshot(out_dir) or load_previous_snapshot(snapshot_dir)
    records: list[dict[str, Any]] = []
    for repo in repo_names:
        print(f"Collecting {repo}...", file=sys.stderr)
        try:
            record = repo_record(repo, token, args.include_readme)
        except RuntimeError as exc:
            if repo not in tracked_records:
                raise
            print(f"Keeping last known metadata for {repo}: {exc}", file=sys.stderr)
            record = dict(tracked_records[repo])
        record["snapshot_date"] = date
        record["sources"] = sources[repo]
        record["trending_stars_today"] = trending_repos.get(repo, {}).get("trending_stars_today")
        records.append(record)

    add_deltas(records, previous)
    mark_new_entries(records, set(historical_records), set(seed_repos + discovered + list(trending_repos)))
    for record in records:
        record["category"] = classify(record)

    payload = {"snapshot_date": date, "repos": sorted(records, key=lambda row: row["full_name"])}
    (out_dir / "repos.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (snapshot_dir / f"repos-{date}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "report.md").write_text(markdown_report(records, queries, seed_repos, date), encoding="utf-8")
    if args.db:
        conn = init_db(Path(args.db))
        try:
            write_db(conn, records, queries, discovered_by_query, date)
        finally:
            conn.close()

    print(textwrap.dedent(f"""
    Wrote:
      {out_dir / 'repos.json'}
      {out_dir / 'report.md'}
      {snapshot_dir / f'repos-{date}.json'}
      {args.db if args.db else '(no sqlite db requested)'}
    """).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
