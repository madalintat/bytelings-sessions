"""Rung 4: Solo — solved version.

`parse_env` is a classic line-by-line accumulator:
  1. Split text on newlines.
  2. Strip each line.
  3. Skip empty lines and comment lines (starting with '#').
  4. Skip lines without '=' (no valid assignment).
  5. Use str.partition('=') to split on the FIRST '=' only, preserving
     '=' in values (e.g. "URL=https://x.io/?a=b").
  6. Strip key and value separately.
  7. Assign into a plain dict; later assignments overwrite earlier ones.

`partition` is the right tool here: it always returns a 3-tuple and
never raises on missing delimiters (it returns ('', '', '') if the
separator isn't found, but we skip those lines first).
"""


def parse_env(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        result[key.strip()] = value.strip()
    return result
