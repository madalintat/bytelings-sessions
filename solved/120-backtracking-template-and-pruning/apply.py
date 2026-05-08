"""Rung 5: Apply — solved version.

A completed cheat-sheet. The template_lines are minimal illustrative
skeletons, not runnable code — they're there to jog memory, not to
compile.

Run: uv run python apply.py [dp|greedy|backtracking]
"""
import sys

LENSES: dict[str, dict] = {
    "dp": {
        "signal": (
            "solve(state) is called with the same state more than once,"
            " OR: the answer is the optimum over choices where each"
            " choice reduces to the same shape on a smaller state."
        ),
        "template_lines": [
            "from functools import cache",
            "",
            "@cache",
            "def solve(state):",
            "    if base_case(state): return base_value",
            "    return aggregate(",
            "        cost(c) + solve(next_state(state, c))",
            "        for c in choices(state)",
            "    )",
        ],
        "proof_obligation": (
            "The recurrence is correct — DP is sound if and only if"
            " the recurrence is. No exchange argument needed."
        ),
        "failure_mode": (
            "State space is exponential or has too many independent"
            " dimensions; memoization table doesn't fit. Switch to"
            " backtracking with pruning."
        ),
    },
    "greedy": {
        "signal": (
            "The answer is built step-by-step and there exists a"
            " single local rule (sortable key) whose exchange argument"
            " shows it never needs to be undone."
        ),
        "template_lines": [
            "items = sorted(items, key=greedy_key)",
            "result = []",
            "for item in items:",
            "    if compatible(item, result):",
            "        result.append(item)",
            "return result",
        ],
        "proof_obligation": (
            "Write the exchange argument: assume OPT disagrees with"
            " greedy at step k, swap greedy's choice in, show the"
            " result is still valid and no worse."
        ),
        "failure_mode": (
            "A locally best choice blocks a better global combination."
            " Classic example: coins [1,4,5] for amount 8."
            " Exchange argument fails → fall back to DP."
        ),
    },
    "backtracking": {
        "signal": (
            "The answer is a sequence of choices with a checkable"
            " constraint at each step, and the state space is too"
            " large for a DP table (or the task is to enumerate all"
            " solutions, not just find the optimum)."
        ),
        "template_lines": [
            "def solve(state):",
            "    if state.is_complete(): record(state); return",
            "    for choice in state.legal_choices():",
            "        if not state.can_extend(choice): continue  # prune",
            "        state.apply(choice)",
            "        solve(state)",
            "        state.undo(choice)  # backtrack",
        ],
        "proof_obligation": (
            "Prove can_extend doesn't reject any valid completion."
            " Too-aggressive pruning misses solutions;"
            " too-lax pruning wastes time."
        ),
        "failure_mode": (
            "Subproblems overlap — the same subtree is recomputed"
            " from multiple entry points. Add memoization (bridge"
            " to DP). Example: word break without @cache."
        ),
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
