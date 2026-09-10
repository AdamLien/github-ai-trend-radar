import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("build_dashboard_data.py")
SPEC = importlib.util.spec_from_file_location("build_dashboard_data", SCRIPT)
builder = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(builder)


class DailySnapshotLoaderTests(unittest.TestCase):
    def test_daily_folder_date_is_the_display_date_and_payload_date_is_provenance(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            daily = Path(temporary_directory) / "daily"
            for folder_date, observed_date, stars in (
                ("2026-09-03", "2026-09-04", 10),
                ("2026-09-04", "2026-09-05", 13),
            ):
                folder = daily / folder_date
                folder.mkdir(parents=True)
                (folder / "repos.json").write_text(json.dumps({
                    "snapshot_date": observed_date,
                    "repos": [{"full_name": "example/radar", "stars": stars}],
                }))

            snapshots = builder.load_daily_snapshots(daily)

        self.assertEqual([snapshot["targetDate"] for snapshot in snapshots], ["2026-09-03", "2026-09-04"])
        self.assertEqual(snapshots[0]["observedDate"], "2026-09-04")

    def test_daily_snapshot_loader_rejects_an_invalid_target_date(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            daily = Path(temporary_directory) / "daily"
            folder = daily / "not-a-date"
            folder.mkdir(parents=True)
            (folder / "repos.json").write_text(json.dumps({"snapshot_date": "2026-09-04", "repos": []}))

            with self.assertRaisesRegex(ValueError, "target date"):
                builder.load_daily_snapshots(daily)

    def test_work_scenarios_are_independent_from_technical_tags(self):
        scenarios = builder.work_scenarios_for({
            "full_name": "example/knowledge-agent",
            "description": "RAG knowledge base with document retrieval and workflow automation.",
            "topics": ["llm", "mcp"],
        })

        self.assertEqual(scenarios, ["文件整理與知識查詢", "資料整合與報表", "內容製作與辦公自動化"])


if __name__ == "__main__":
    unittest.main()
