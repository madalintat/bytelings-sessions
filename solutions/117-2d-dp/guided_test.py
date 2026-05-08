"""Tests for rung 3 — is_safe and n_queens_guided."""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_is_safe_empty():
    diagnose(
        ex.is_safe(0, 0, []) is True,
        "First queen on empty board should always be safe.",
        (lambda: ex.is_safe(0, 0, []) is False,
         "With no placed queens, any cell is safe — return True when cols is empty."),
    )


def test_is_safe_same_column():
    diagnose(
        ex.is_safe(1, 0, [0]) is False,
        "is_safe(1, 0, [0]) should be False — column 0 is already taken.",
        (lambda: ex.is_safe(1, 0, [0]) is True,
         "Column 0 is occupied by the queen at row 0. Same-column attacks "
         "are checked with cols[r] == col."),
    )


def test_is_safe_diagonal():
    # Queen at row 0, col 0 → (1, 1) is on the diagonal
    diagnose(
        ex.is_safe(1, 1, [0]) is False,
        "is_safe(1, 1, [0]) should be False — diagonal attack from (0, 0).",
        (lambda: ex.is_safe(1, 1, [0]) is True,
         "abs(1-0) == abs(1-0) → same diagonal. "
         "Check abs(row - r) == abs(col - cols[r])."),
    )


def test_is_safe_anti_diagonal():
    # Queen at row 0, col 2 → (1, 1) is on the anti-diagonal
    diagnose(
        ex.is_safe(1, 1, [2]) is False,
        "is_safe(1, 1, [2]) should be False — anti-diagonal attack.",
        (lambda: ex.is_safe(1, 1, [2]) is True,
         "abs(1-0) == abs(1-2) → anti-diagonal. "
         "The abs() handles both diagonals at once."),
    )


def test_is_safe_clear():
    # Queen at row 0, col 0 → (2, 1) is safe
    diagnose(
        ex.is_safe(2, 1, [0]) is True,
        "is_safe(2, 1, [0]) should be True — (2,1) is not attacked by (0,0).",
        (lambda: ex.is_safe(2, 1, [0]) is False,
         "(2,1) is not in the same column or diagonal as (0,0). "
         "abs(2-0)=2, abs(1-0)=1 — not equal, no diagonal attack."),
    )


def test_n4_count():
    solutions = ex.n_queens_guided(4)
    diagnose(
        len(solutions) == 2,
        f"N=4 has exactly 2 solutions, got {len(solutions)}.",
        (lambda: len(solutions) == 0,
         "No solutions found — is_safe is probably too strict (always False?)."),
        (lambda: len(solutions) > 2,
         "Too many solutions — is_safe is too permissive. "
         "Check that BOTH same-column and diagonal attacks are blocked."),
    )


def test_n4_solutions_valid():
    solutions = ex.n_queens_guided(4)
    for sol in solutions:
        # each col index is unique (no column conflict)
        assert len(set(sol)) == 4, f"Column conflict in solution {sol}"
        # no diagonal conflicts
        for i in range(len(sol)):
            for j in range(i + 1, len(sol)):
                assert abs(i - j) != abs(sol[i] - sol[j]), (
                    f"Diagonal conflict between rows {i} and {j} in {sol}"
                )


def test_n1():
    assert ex.n_queens_guided(1) == [[0]]


def test_n2_no_solutions():
    assert ex.n_queens_guided(2) == []
