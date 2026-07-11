#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
DEST="$CODEX_HOME/skills"

mkdir -p "$DEST"

for skill_dir in "$REPO_ROOT"/skills/*; do
  [[ -d "$skill_dir" ]] || continue
  name="$(basename "$skill_dir")"
  target="$DEST/$name"
  if [[ -L "$target" || -e "$target" ]]; then
    rm -rf "$target"
  fi
  ln -s "$skill_dir" "$target"
  echo "linked $name -> $target"
done
