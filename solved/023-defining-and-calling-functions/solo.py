"""Rung 4: Solo — solved version.

`parse_flags` is a small state-machine over the args list:
  - Walk args with an index (manual `while i < len(args)` loop).
  - Recognize `--flag=value` (split on first '=') vs. `--flag value`
    (consume the next token).
  - `--verbose` is a boolean flag.
  - `--out` and `--count` consume the next token if no `=value` present.
  - Raise ValueError for unknown flags (unless allow_unknown=True) and
    for missing or non-integer values.

The sentinel default `result` is built upfront so the return dict is
always fully populated.
"""


def parse_flags(args: list[str], allow_unknown: bool = False) -> dict:
    result = {"verbose": False, "out": None, "count": None}
    i = 0
    while i < len(args):
        token = args[i]
        if "=" in token:
            flag, _, value = token.partition("=")
        else:
            flag = token
            value = None

        if flag == "--verbose":
            result["verbose"] = True
        elif flag == "--out":
            if value is None:
                i += 1
                if i >= len(args):
                    raise ValueError("--out requires a value")
                value = args[i]
            result["out"] = value
        elif flag == "--count":
            if value is None:
                i += 1
                if i >= len(args):
                    raise ValueError("--count requires a value")
                value = args[i]
            try:
                result["count"] = int(value)
            except (ValueError, TypeError):
                raise ValueError(f"--count requires an integer, got {value!r}")
        elif flag.startswith("--"):
            if not allow_unknown:
                raise ValueError(f"unknown flag: {flag}")
        i += 1
    return result
