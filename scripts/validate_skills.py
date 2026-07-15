#!/usr/bin/env python3
"""Validate local Codex skill folders without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$")
LOCAL_REF_RE = re.compile(
    r"`(references/[^`]+?\.md)`|\]\((references/[^)#]+?\.md)(?:#[^)]+)?\)"
)
AGENT_FIELD_RE = re.compile(r'^\s{2}([a-z_]+):\s*"([^"]*)"\s*$', re.MULTILINE)
NAME_RE = re.compile(r"^[a-z0-9-]{1,63}$")


def parse_frontmatter(skill_md: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, ["missing YAML frontmatter"]

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        field = FIELD_RE.match(line)
        if not field:
            errors.append(f"invalid frontmatter line: {line}")
            continue
        key, value = field.groups()
        fields[key] = value.strip().strip('"').strip("'")

    extra = sorted(set(fields) - {"name", "description"})
    if extra:
        errors.append(f"unexpected frontmatter fields: {', '.join(extra)}")
    if "name" not in fields:
        errors.append("missing frontmatter name")
    if "description" not in fields:
        errors.append("missing frontmatter description")
    return fields, errors


def local_refs(markdown: Path) -> set[str]:
    text = markdown.read_text(encoding="utf-8")
    refs: set[str] = set()
    for match in LOCAL_REF_RE.finditer(text):
        refs.add(next(group for group in match.groups() if group))
    return refs


def parse_agent(agent_yaml: Path) -> dict[str, str]:
    text = agent_yaml.read_text(encoding="utf-8")
    return {key: value for key, value in AGENT_FIELD_RE.findall(text)}


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["missing SKILL.md"]

    fields, fm_errors = parse_frontmatter(skill_md)
    errors.extend(fm_errors)

    name = fields.get("name", "")
    if name and not NAME_RE.match(name):
        errors.append(f"invalid skill name: {name}")
    if name and name != skill_dir.name:
        errors.append(f"frontmatter name {name!r} does not match folder {skill_dir.name!r}")
    if fields.get("description", "").strip() == "":
        errors.append("empty description")

    line_count = len(skill_md.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        errors.append(f"SKILL.md has {line_count} lines; expected <= 500")

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if not agent_yaml.exists():
        errors.append("missing agents/openai.yaml")
    else:
        agent_fields = parse_agent(agent_yaml)
        for required in ("display_name", "short_description", "default_prompt"):
            if not agent_fields.get(required):
                errors.append(f"missing agents/openai.yaml interface.{required}")
        short_description = agent_fields.get("short_description", "")
        if short_description and not (25 <= len(short_description) <= 80):
            errors.append(
                "interface.short_description should be concise "
                f"(25-80 chars here), got {len(short_description)}"
            )
        default_prompt = agent_fields.get("default_prompt", "")
        if name and f"${name}" not in default_prompt:
            errors.append(f"default_prompt does not mention ${name}")

    references_dir = skill_dir / "references"
    if not references_dir.exists():
        errors.append("missing references directory")
    else:
        refs = sorted(references_dir.glob("*.md"))
        if not refs:
            errors.append("references directory has no markdown files")
        if not (references_dir / "forward-tests.md").exists():
            errors.append("missing references/forward-tests.md")

        skill_refs = local_refs(skill_md)
        actual_refs = {f"references/{path.name}" for path in refs}
        missing_from_skill = sorted(actual_refs - skill_refs)
        if missing_from_skill:
            errors.append(
                "reference files not directly discoverable from SKILL.md: "
                + ", ".join(missing_from_skill)
            )

        for markdown in [skill_md, *refs]:
            for ref in sorted(local_refs(markdown)):
                if not (skill_dir / ref).exists():
                    errors.append(f"{markdown.relative_to(skill_dir)} links missing {ref}")

    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path("skills")
    if not root.exists():
        print(f"error: {root} does not exist", file=sys.stderr)
        return 2

    skill_dirs = sorted(path for path in root.iterdir() if path.is_dir())
    if not skill_dirs:
        print(f"error: no skill directories found in {root}", file=sys.stderr)
        return 2

    total_errors = 0
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            total_errors += len(errors)
            print(f"FAIL {skill_dir}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {skill_dir}")

    if total_errors:
        print(f"\n{total_errors} validation issue(s) found.")
        return 1

    print(f"\nValidated {len(skill_dirs)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
