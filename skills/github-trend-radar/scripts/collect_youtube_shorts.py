#!/usr/bin/env python3
"""Track public YouTube Shorts metadata from a channel's Shorts page."""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DEFAULT_CHANNEL_URL = "https://www.youtube.com/@Oraink%E7%81%B5%E7%A0%9A/shorts"
DEFAULT_CHANNEL_ID = "UC7nSdrHf_8k9JzDBxbO-kDQ"


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def extract_shorts(payload: dict) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    for node in walk(payload):
        model = node.get("shortsLockupViewModel")
        if not isinstance(model, dict):
            continue
        video_id = model.get("onTap", {}).get("innertubeCommand", {}).get("reelWatchEndpoint", {}).get("videoId")
        if not isinstance(video_id, str) or not video_id or video_id in seen:
            continue
        accessibility = model.get("accessibilityText", "")
        title = re.split(r",\s*(?:觀看次數|views?)[:：]", accessibility, maxsplit=1, flags=re.I)[0].strip()
        views = re.search(r"(?:觀看次數|views?)[:：]\s*([^\s,，-]+)", accessibility, flags=re.I)
        items.append({
            "videoId": video_id,
            "title": title or video_id,
            "url": f"https://www.youtube.com/shorts/{video_id}",
            "viewsText": views.group(1) if views else "",
        })
        seen.add(video_id)
    return items


def parse_initial_data(html: str) -> dict:
    marker = "var ytInitialData = "
    start = html.find(marker)
    if start < 0:
        raise ValueError("YouTube page did not expose initial Shorts data")
    raw = html[start + len(marker):]
    payload, _ = json.JSONDecoder().raw_decode(raw)
    if not isinstance(payload, dict):
        raise ValueError("YouTube initial Shorts data is not an object")
    return payload


def previous_ids(out_dir: Path) -> set[str]:
    daily = out_dir.parent
    candidates = sorted(path for path in daily.iterdir() if path.is_dir() and path.name < out_dir.name)
    if not candidates:
        return set()
    latest = candidates[-1] / "videos.json"
    if not latest.exists():
        return set()
    payload = json.loads(latest.read_text(encoding="utf-8"))
    return {item["videoId"] for item in payload.get("items", []) if item.get("videoId")}


def fetch_html(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; metabiz-radar/1.0)"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--target-date", default=datetime.now(ZoneInfo("Asia/Taipei")).date().isoformat())
    parser.add_argument("--channel-url", default=DEFAULT_CHANNEL_URL)
    parser.add_argument("--channel-id", default=DEFAULT_CHANNEL_ID)
    args = parser.parse_args()

    out_dir = args.out
    out_dir.mkdir(parents=True, exist_ok=True)
    prior = previous_ids(out_dir)
    items = extract_shorts(parse_initial_data(fetch_html(args.channel_url)))
    for item in items:
        item["isNew"] = item["videoId"] not in prior
    payload = {
        "targetDate": args.target_date,
        "capturedAt": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(timespec="seconds"),
        "channel": {"name": "Oraink", "channelId": args.channel_id, "shortsUrl": args.channel_url},
        "items": items,
    }
    (out_dir / "videos.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    snapshots = out_dir / "snapshots"
    snapshots.mkdir(exist_ok=True)
    (snapshots / f"videos-{args.target_date}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    new_count = sum(item["isNew"] for item in items)
    lines = [f"# Oraink Shorts 追蹤（{args.target_date}）", "", f"- 公開頻道：{args.channel_url}", f"- 擷取到 {len(items)} 則；相較前一快照新增 {new_count} 則。", "- 注意：YouTube Shorts 頁面未穩定提供所有發布時間；此報表記錄抓取時間與首次觀測，不把觀看數當作發布日期。", ""]
    for item in items:
        marker = "新增" if item["isNew"] else "持續追蹤"
        lines.append(f"- [{marker}] [{item['title']}]({item['url']})" + (f"（頁面顯示 {item['viewsText']}）" if item["viewsText"] else ""))
    (out_dir / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Tracked {len(items)} Shorts ({new_count} new) in {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
