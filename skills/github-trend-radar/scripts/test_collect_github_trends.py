import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).with_name("collect_github_trends.py")
SPEC = importlib.util.spec_from_file_location("collect_github_trends", SCRIPT)
collector = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(collector)


def test_trending_parser_keeps_scoped_repositories_and_daily_star_signal():
    html = """
    <article class="Box-row">
      <h2><a href="/example/new-mcp-server">example / new-mcp-server</a></h2>
      <p>A Model Context Protocol server for document AI automation.</p>
      <span>321 stars today</span>
    </article>
    <article class="Box-row">
      <h2><a href="/example/game">example / game</a></h2>
      <p>A retro game engine.</p>
      <span>999 stars today</span>
    </article>
    """

    assert collector.parse_trending_daily(html) == {
        "example/new-mcp-server": {"trending_stars_today": 321}
    }


def test_merge_sources_marks_first_trending_appearance_as_new():
    sources = collector.merge_sources(
        ["example/search-hit"],
        {"example/search-hit": {"trending_stars_today": 12}, "example/new-mcp-server": {"trending_stars_today": 321}},
    )

    assert sources["example/search-hit"] == ["search", "trending_daily"]
    assert sources["example/new-mcp-server"] == ["trending_daily"]


def test_add_deltas_marks_first_appearance_as_new():
    records = [{"full_name": "example/new-mcp-server", "stars": 321, "forks": 0}]

    collector.add_deltas(records, {})

    assert records[0]["is_new"] is True
    assert records[0]["stars_delta"] == 0


def test_trending_parser_ignores_sponsor_links_outside_the_heading():
    html = """
    <article class="Box-row">
      <a href="/sponsors/example">Sponsor</a>
      <h2><a href="/example/mcp-automation">example / mcp-automation</a></h2>
      <p>Automate developer workflows with MCP.</p>
      <span>44 stars today</span>
    </article>
    """

    assert collector.parse_trending_daily(html) == {
        "example/mcp-automation": {"trending_stars_today": 44}
    }


def test_previous_daily_snapshot_uses_prior_target_folder(tmp_path):
    daily = tmp_path / "daily"
    previous = daily / "2026-08-10"
    current = daily / "2026-08-11"
    previous.mkdir(parents=True)
    current.mkdir()
    (previous / "repos.json").write_text('{"repos": [{"full_name": "example/old", "stars": 10}]}')
    (current / "repos.json").write_text('{"repos": [{"full_name": "example/current", "stars": 20}]}')

    assert collector.load_previous_daily_snapshot(current) == {
        "example/old": {"full_name": "example/old", "stars": 10}
    }


def test_tracked_repositories_accumulate_across_all_prior_daily_folders(tmp_path):
    daily = tmp_path / "daily"
    for name, repo in (("2026-08-09", "example/first"), ("2026-08-10", "example/second")):
        folder = daily / name
        folder.mkdir(parents=True)
        (folder / "repos.json").write_text('{"repos": [{"full_name": "' + repo + '", "stars": 1}]}')
    current = daily / "2026-08-11"
    current.mkdir()

    assert collector.load_tracked_repo_names(current) == {"example/first", "example/second"}


def test_tracked_records_keep_latest_known_metadata_when_a_refresh_fails(tmp_path):
    daily = tmp_path / "daily"
    for name, stars in (("2026-08-09", 10), ("2026-08-10", 20)):
        folder = daily / name
        folder.mkdir(parents=True)
        (folder / "repos.json").write_text('{"repos": [{"full_name": "example/first", "stars": ' + str(stars) + '}]}')
    current = daily / "2026-08-11"
    current.mkdir()

    assert collector.load_tracked_records(current)["example/first"]["stars"] == 20


def test_new_entry_requires_current_discovery_and_absence_from_prior_history():
    records = [
        {"full_name": "example/historical", "stars": 10, "forks": 0},
        {"full_name": "example/new-trending", "stars": 20, "forks": 0},
    ]

    collector.mark_new_entries(records, {"example/historical"}, {"example/historical", "example/new-trending"})

    assert records[0]["is_new"] is False
    assert records[1]["is_new"] is True


def test_pinned_watchlist_repository_is_retained_with_explicit_source():
    sources = collector.merge_sources(
        ["example/search-hit"],
        {},
        ["stablyai/orca"],
    )

    assert sources["stablyai/orca"] == ["pinned_watchlist"]


def test_tracked_records_include_current_target_on_a_rerun(tmp_path):
    daily = tmp_path / "daily"
    current = daily / "2026-08-11"
    current.mkdir(parents=True)
    (current / "repos.json").write_text('{"repos": [{"full_name": "example/current", "stars": 20}]}')

    assert collector.load_tracked_records(current)["example/current"]["stars"] == 20

