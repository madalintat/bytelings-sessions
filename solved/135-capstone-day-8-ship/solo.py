"""Rung 4: Solo — solved version.

P-07 accumulator-into-dict: build count dicts by iterating once over
findings, then sort by count descending (ties broken alphabetically).
"""
from __future__ import annotations


def summary(findings: list[dict]) -> str:
    """Return a multi-line graduation-log summary block."""
    # Accumulate counts (P-07)
    by_rule: dict[str, int] = {}
    by_file: dict[str, int] = {}
    for f in findings:
        by_rule[f["rule"]] = by_rule.get(f["rule"], 0) + 1
        by_file[f["path"]] = by_file.get(f["path"], 0) + 1

    # Sort: count desc, then key asc for ties
    sorted_rules = sorted(by_rule.items(), key=lambda kv: (-kv[1], kv[0]))
    sorted_files = sorted(by_file.items(), key=lambda kv: (-kv[1], kv[0]))

    lines = [
        "=== Linter Findings Summary ===",
        f"Total: {len(findings)} findings",
        "",
        "By rule (most frequent first):",
    ]
    for rule, count in sorted_rules:
        lines.append(f"  {rule}: {count}")

    lines.append("")
    lines.append("Top 3 affected files:")
    for path, count in sorted_files[:3]:
        lines.append(f"  {path}: {count} finding(s)")

    return "\n".join(lines)
