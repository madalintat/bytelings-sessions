"""Rung 5: Apply — refactored categorize_users with _bucket_for helper.

The original bug: a user with logins_30d >= 5 who is also banned would
land in BOTH "active" and "banned" because the `if logins >= 5` ran
unconditionally before the banned check. Extracting _bucket_for() that
returns exactly ONE label makes the mutual-exclusion explicit.

The refactor: each function is <= 12 body lines (enforced by the
AST-based style check in main()).

Run it:
    uv run python apply.py
"""
from __future__ import annotations

import ast
from pathlib import Path


# ---- refactored functions ------------------------------------------

def _bucket_for(user: dict) -> str:
    """Return the single bucket label for one user."""
    if user.get("banned") is True:
        return "banned"
    logins = user.get("logins_30d", 0)
    if logins >= 5:
        return "active"
    if logins == 0:
        return "dormant"
    return "casual"


def categorize_users(users: list[dict]) -> dict:
    """Bucket users by activity. Returns a dict with these keys:

      "active":   users with >= 5 logins in the last 30 days, NOT banned
      "dormant":  users with 0 logins in the last 30 days, NOT banned
      "casual":   anyone else (1..4 logins) NOT banned
      "banned":   users where banned == True (regardless of logins)

    Each bucket value is a list of user "id" strings, sorted ascending.
    """
    buckets: dict[str, list[str]] = {
        "active": [], "dormant": [], "casual": [], "banned": [],
    }
    for u in users:
        buckets[_bucket_for(u)].append(u["id"])
    return {k: sorted(v) for k, v in buckets.items()}


# ---- assertions and style check ------------------------------------

def _ast_function_lengths(source_path: Path) -> dict[str, int]:
    """Return {function_name: body_line_count} for top-level fns in source."""
    tree = ast.parse(source_path.read_text())
    out: dict[str, int] = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            body = node.body
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant):
                body = body[1:]
            if not body:
                out[node.name] = 0
                continue
            start = body[0].lineno
            end = body[-1].end_lineno or body[-1].lineno
            out[node.name] = end - start + 1
    return out


def main() -> None:
    users = [
        {"id": "u-alice",   "logins_30d": 12, "banned": False},
        {"id": "u-bob",     "logins_30d": 0,  "banned": False},
        {"id": "u-carol",   "logins_30d": 3,  "banned": False},
        {"id": "u-dan",     "logins_30d": 0,  "banned": True},
        {"id": "u-eve",     "logins_30d": 8,  "banned": True},
        {"id": "u-frank",                        "banned": False},
    ]
    out = categorize_users(users)

    assert out["active"] == ["u-alice"], f"active wrong: {out['active']!r}"
    assert out["dormant"] == ["u-bob", "u-frank"], f"dormant wrong: {out['dormant']!r}"
    assert out["casual"] == ["u-carol"], f"casual wrong: {out['casual']!r}"
    assert out["banned"] == ["u-dan", "u-eve"], f"banned wrong: {out['banned']!r}"

    lengths = _ast_function_lengths(Path(__file__))
    long_fns = {n: ll for n, ll in lengths.items() if ll > 12}
    assert not long_fns, (
        f"Functions exceeding 12 body lines: {long_fns}. "
        "Extract a helper. The point of this exercise is naming the pieces."
    )

    print("categorize_users behaves correctly + every function <= 12 lines.")
    for name, ll in lengths.items():
        print(f"  {name}: {ll} body lines")


if __name__ == "__main__":
    main()
