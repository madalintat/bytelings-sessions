"""Rung 4: Solo implement — solved version.

Walk lines, skip blanks and comments, strip whitespace around key/value,
raise ValueError on lines missing '=', last writer wins for duplicates.
"""


def parse_kv(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            raise ValueError(f"malformed line: {stripped}")
        key, value = stripped.split("=", 1)
        result[key.strip()] = value.strip()
    return result
