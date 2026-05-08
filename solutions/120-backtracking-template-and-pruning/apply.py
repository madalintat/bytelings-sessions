"""Rung 5: Apply — three-lens cheat-sheet.

This module IS the exercise. Fill in the `LENSES` dict with your own
understanding of each lens, then run:

    uv run python apply.py <lens-name>

to pretty-print the matching entry.

Run without arguments to see all three lenses.
"""
import sys
from pprint import pformat

# TODO: Fill in each dict. Keys are:
#   "signal"           — one sentence: how do you recognise this lens?
#   "template_lines"   — list[str] of the canonical code skeleton
#   "proof_obligation" — what must you prove/verify for correctness?
#   "failure_mode"     — what breaks when the wrong lens is applied?

LENSES: dict[str, dict] = {
    "dp": {
        "signal": "TODO: recognition signal for DP",
        "template_lines": [
            "# TODO: fill in the DP template",
        ],
        "proof_obligation": "TODO: what must hold for DP correctness?",
        "failure_mode": "TODO: what goes wrong when DP is the wrong choice?",
    },
    "greedy": {
        "signal": "TODO: recognition signal for greedy",
        "template_lines": [
            "# TODO: fill in the greedy template",
        ],
        "proof_obligation": "TODO: what must you prove for greedy correctness?",
        "failure_mode": "TODO: what goes wrong when greedy fails?",
    },
    "backtracking": {
        "signal": "TODO: recognition signal for backtracking",
        "template_lines": [
            "# TODO: fill in the backtracking template",
        ],
        "proof_obligation": "TODO: what must your pruning predicate satisfy?",
        "failure_mode": "TODO: what goes wrong with overlapping subproblems?",
    },
}


def _print_lens(name: str) -> None:
    entry = LENSES.get(name)
    if entry is None:
        print(f"Unknown lens {name!r}. Choose: dp, greedy, backtracking")
        sys.exit(1)
    print(f"\n=== {name.upper()} ===")
    print(f"Signal:            {entry['signal']}")
    print(f"Proof obligation:  {entry['proof_obligation']}")
    print(f"Failure mode:      {entry['failure_mode']}")
    print("Template:")
    for line in entry["template_lines"]:
        print(f"  {line}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        _print_lens(sys.argv[1])
    else:
        for lens in ("dp", "greedy", "backtracking"):
            _print_lens(lens)
