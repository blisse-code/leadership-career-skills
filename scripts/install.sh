#!/usr/bin/env bash
# Install the skills into Claude Code without the plugin system.
#
#   ./scripts/install.sh                 # all skills, user scope (~/.claude/skills)
#   ./scripts/install.sh --project       # all skills, current project (./.claude/skills)
#   ./scripts/install.sh leadership-storytelling ux-leadership-case-study   # only these
#
# One-liner without cloning:
#   curl -fsSL https://raw.githubusercontent.com/blisse-code/leadership-career-skills/main/scripts/install.sh | bash
set -euo pipefail

REPO_URL="https://github.com/blisse-code/leadership-career-skills"
DEST="${HOME}/.claude/skills"
SELECTED=()

for arg in "$@"; do
  case "$arg" in
    --project) DEST="$(pwd)/.claude/skills" ;;
    -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
    *) SELECTED+=("$arg") ;;
  esac
done

# Locate the skills: this checkout if we're in it, otherwise a temporary clone.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || echo "")"
SRC=""
if [ -n "$SCRIPT_DIR" ] && [ -d "$SCRIPT_DIR/../plugins/leadership-career-skills/skills" ]; then
  SRC="$SCRIPT_DIR/../plugins/leadership-career-skills/skills"
else
  command -v git >/dev/null || { echo "git is required"; exit 1; }
  TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
  git clone --depth 1 -q "$REPO_URL" "$TMP/repo"
  SRC="$TMP/repo/plugins/leadership-career-skills/skills"
fi

mkdir -p "$DEST"
if [ ${#SELECTED[@]} -eq 0 ]; then
  for d in "$SRC"/*/; do SELECTED+=("$(basename "$d")"); done
fi

for s in "${SELECTED[@]}"; do
  if [ ! -f "$SRC/$s/SKILL.md" ]; then echo "skip: unknown skill '$s'"; continue; fi
  if [ -d "$DEST/$s" ]; then
    mv "$DEST/$s" "$DEST/$s.bak.$(date +%Y%m%d%H%M%S)"
    echo "backed up existing $s"
  fi
  cp -R "$SRC/$s" "$DEST/$s"
  echo "installed $s -> $DEST/$s"
done
echo "Done. Start a new Claude Code session and run /skills to confirm."
