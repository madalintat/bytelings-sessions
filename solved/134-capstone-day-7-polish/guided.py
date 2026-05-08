"""Rung 3: Guided — solved version.

Scan lines for 'environment:', then scan the lines that follow (while
they are indented more than the trigger line) looking for 'url:'.
Return the stripped value after 'url:' or None if not found.
"""
from __future__ import annotations


def extract_pypi_url(yaml_str: str) -> str | None:
    """Return the URL from the environment block, or None if absent."""
    lines = yaml_str.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if "environment:" in line:
            # Scan subsequent indented lines for 'url:'
            j = i + 1
            while j < len(lines) and (not lines[j].strip() or lines[j].startswith(" ")):
                if "url:" in lines[j]:
                    _, _, value = lines[j].partition("url:")
                    return value.strip()
                j += 1
        i += 1
    return None
