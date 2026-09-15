#!/usr/bin/env bash
set -Eeuo pipefail
umask 077

project=/home/metabiz-admin/Documents/workspace/adam-codex-skills
config=/home/metabiz-admin/.config/github-trend-radar
target_date="$(TZ=Asia/Taipei date +%F)"

mkdir -p "$config"
exec 9>"$config/oraink-shorts.lock"
if ! flock -n 9; then
  printf 'Oraink Shorts tracker is already running; skip duplicate invocation.\n' >&2
  exit 0
fi

cd "$project"
exec python3 skills/github-trend-radar/scripts/collect_youtube_shorts.py \
  --target-date "$target_date" \
  --out "outputs/youtube-radar/oraink/daily/$target_date"
