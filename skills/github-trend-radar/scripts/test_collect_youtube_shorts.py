import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).with_name("collect_youtube_shorts.py")
SPEC = importlib.util.spec_from_file_location("youtube_shorts", SCRIPT)
collector = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(collector)


class YouTubeShortsParserTests(unittest.TestCase):
    def test_extracts_shorts_metadata_without_treating_views_as_upload_date(self):
        payload = {
            "shortsLockupViewModel": {
                "entityId": "shorts-shelf-item-demo123",
                "accessibilityText": "GitHub AI weekly roundup, 觀看次數：1.2萬次 - 播放 Shorts",
                "onTap": {"innertubeCommand": {"reelWatchEndpoint": {"videoId": "demo123"}}},
            }
        }

        items = collector.extract_shorts(payload)

        self.assertEqual(items[0]["videoId"], "demo123")
        self.assertEqual(items[0]["title"], "GitHub AI weekly roundup")
        self.assertEqual(items[0]["viewsText"], "1.2萬次")
        self.assertNotIn("publishedAt", items[0])


if __name__ == "__main__":
    unittest.main()
