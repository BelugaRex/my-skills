#!/usr/bin/env python3
"""Validate all skills in this repo: frontmatter, name/dir match, link targets."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
errors = []

for skill_md in sorted(ROOT.glob("*/SKILL.md")):
    d = skill_md.parent
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        errors.append(f"{d.name}: missing frontmatter block")
        continue
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc_m = re.search(r"^description:\s*(\S.*)$", fm, re.M)
    if not name_m:
        errors.append(f"{d.name}: frontmatter missing 'name'")
    elif name_m.group(1) != d.name:
        errors.append(f"{d.name}: name '{name_m.group(1)}' != directory name")
    if not desc_m:
        errors.append(f"{d.name}: frontmatter missing 'description'")
    for link in re.findall(r"\]\(([^)#]+?\.md)\)", text):
        if link.startswith(("http://", "https://")):
            continue
        if not (d / link).exists():
            errors.append(f"{d.name}: broken link target {link}")

for ref in ROOT.glob("*/references/*.md"):
    if ref.stat().st_size == 0:
        errors.append(f"{ref.relative_to(ROOT)}: empty file")

if errors:
    print("FAIL")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("PASS: all skills valid")
