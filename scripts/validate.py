#!/usr/bin/env python3
"""Validate every skill in the repo (Claude and ChatGPT editions).

Checks, per SKILL.md:
  - YAML frontmatter present with `name` and `description`
  - name is lowercase letters, digits, hyphens; matches its folder
  - description is 1..1024 characters and contains no angle brackets
  - every `references/...` or `scripts/...` path mentioned in SKILL.md exists
  - SKILL.md body under 500 lines (warning only)
Exit code 1 on any error. Standard library only.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL_DIRS = [ROOT / "plugins/leadership-career-skills/skills", ROOT / "chatgpt/skills"]

errors, warnings = [], []


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


for base in SKILL_DIRS:
    for skill in sorted(p for p in base.iterdir() if p.is_dir()):
        md = skill / "SKILL.md"
        rel = md.relative_to(ROOT)
        if not md.exists():
            errors.append(f"{rel}: missing")
            continue
        text = md.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if not fm:
            errors.append(f"{rel}: no YAML frontmatter")
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
            errors.append(f"{rel}: bad name '{name}'")
        if name != skill.name:
            errors.append(f"{rel}: name '{name}' != folder '{skill.name}'")
        if not 0 < len(desc) <= 1024:
            errors.append(f"{rel}: description length {len(desc)} (must be 1..1024)")
        if "<" in desc or ">" in desc:
            errors.append(f"{rel}: description contains angle brackets")
        for ref in set(re.findall(r"`((?:references|scripts)/[\w./-]+)`", text)):
            if not (skill / ref).exists():
                errors.append(f"{rel}: referenced file missing: {ref}")
        n = text.count("\n")
        if n > 500:
            warnings.append(f"{rel}: {n} lines (guideline is under 500)")
        print(f"ok  {rel}  (description {len(desc)} chars)")

for w in warnings:
    print("WARN", w)
for e in errors:
    print("ERROR", e)
sys.exit(1 if errors else 0)
