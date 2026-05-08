"""Rung 5: Apply — refactor a DIFFERENT tangled function, find ITS bug.

Solo had you refactor `analyze_orders`. That bug was in revenue
counting refunded orders. This rung gives you a fresh function:
`categorize_users`. Tests pin its INTENDED behavior — which is NOT
quite what the current code does.

Your job (matches the day's discipline):
  1. Read the code below until you understand it.
  2. Refactor for clarity (extract helpers, rename, kill duplication).
  3. The bug surfaces during step 2. Fix it.
  4. The asserts in main() pin the intended behavior — the same
     contract as the docstring of `categorize_users`.
  5. Soft style check: NO function in this file should exceed 12 lines
     after your refactor (excluding docstring + signature). Apply
     enforces this with an AST-based length check. If it complains,
     extract another helper.

Concept (the day's NEW one — applied to a fresh codebase): refactoring
isn't tidying. It's investigation. Each rename or extraction is a
hypothesis about what the code is really doing. The bug emerges when
the hypothesis lands wrong somewhere — usually at the spot that
resists naming.

Run it:
    uv run python apply.py
"""
from __future__ import annotations

import ast
import inspect
from pathlib import Path


# ---- the tangled function ------------------------------------------

def categorize_users(users: list[dict]) -> dict:
    """Bucket users by activity. Returns a dict with these keys:

      "active":   users with >= 5 logins in the last 30 days, NOT banned
      "dormant":  users with 0 logins in the last 30 days, NOT banned
      "casual":   anyone else (1..4 logins) NOT banned
      "banned":   users where banned == True (regardless of logins)

    Each bucket value is a list of user "id" strings, sorted ascending.

    Current code has a subtle bug — find it during refactoring.
    """
    active = []
    dormant = []
    casual = []
    banned = []
    for u in users:
        if u.get("logins_30d", 0) >= 5:
            active.append(u["id"])
        if u.get("banned") == True:
            banned.append(u["id"])
        elif u.get("logins_30d", 0) == 0:
            dormant.append(u["id"])
        else:
            casual.append(u["id"])
    return {
        "active": sorted(active),
        "dormant": sorted(dormant),
        "casual": sorted(casual),
        "banned": sorted(banned),
    }


# ---- assertions and style check ------------------------------------

def _ast_function_lengths(source_path: Path) -> dict[str, int]:
    """Return {function_name: body_line_count} for top-level fns in source."""
    tree = ast.parse(source_path.read_text())
    out: dict[str, int] = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            # body lines, excluding the docstring node if present
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
        {"id": "u-dan",     "logins_30d": 0,  "banned": True},   # banned, was dormant
        {"id": "u-eve",     "logins_30d": 8,  "banned": True},   # banned, was active
        {"id": "u-frank",                        "banned": False},  # missing logins_30d → 0 → dormant
    ]
    out = categorize_users(users)

    assert out["active"] == ["u-alice"], f"active wrong: {out['active']!r}"
    assert out["dormant"] == ["u-bob", "u-frank"], f"dormant wrong: {out['dormant']!r}"
    assert out["casual"] == ["u-carol"], f"casual wrong: {out['casual']!r}"
    assert out["banned"] == ["u-dan", "u-eve"], f"banned wrong: {out['banned']!r}"

    # The bug to find: in the original code, banned users could end up in
    # BOTH buckets if their activity matched. The asserts above check that
    # a banned user appears ONLY in "banned". If you hit a duplicate, your
    # refactor needs to make the bucket choice mutually exclusive — usually
    # by extracting a `_bucket_for(user)` helper that returns one label.

    # Style check: extracting helpers should keep each function ≤ 12 body lines.
    lengths = _ast_function_lengths(Path(__file__))
    long_fns = {n: ll for n, ll in lengths.items() if ll > 12}
    assert not long_fns, (
        f"Functions exceeding 12 body lines: {long_fns}. "
        "Extract a helper. The point of this exercise is naming the pieces."
    )

    print("✓ categorize_users behaves correctly + every function ≤ 12 lines.")
    for name, ll in lengths.items():
        print(f"  {name}: {ll} body lines")


if __name__ == "__main__":
    main()
