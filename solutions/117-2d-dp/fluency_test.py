"""Tests for rung 2 — N-queens safe cells.

Confirms that safe_cells correctly marks which positions are unattacked.
"""
import importlib.util
from pathlib import Path

from _byte import diagnose

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_2"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "fluency.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def test_empty_board():
    result = ex.safe_cells(4, [])
    expected = {(r, c) for r in range(4) for c in range(4)}
    diagnose(
        result == expected,
        f"With no queens placed all 16 cells should be safe, got {len(result)}.",
        (lambda: len(result) != 16,
         "Empty board should return all N*N = 16 cells. Count the cells "
         "in the set — you may be filtering too aggressively."),
    )


def test_single_queen_col_blocked():
    # Queen at (0, 1) — column 1 and its diagonals are unsafe
    result = ex.safe_cells(4, [(0, 1)])
    # column 1 entirely blocked
    diagnose(
        all((r, 1) not in result for r in range(4)),
        "Column 1 should be fully blocked by queen at (0, 1).",
        (lambda: (1, 1) in result,
         "(1, 1) is in the same column as the queen at (0, 1) — block it."),
    )


def test_single_queen_diagonal_blocked():
    result = ex.safe_cells(4, [(0, 1)])
    # (1, 2) is on the diagonal of (0, 1): abs(1-0) == abs(2-1)
    diagnose(
        (1, 2) not in result,
        "(1, 2) is on the diagonal of queen at (0, 1) — should be unsafe.",
        (lambda: (1, 0) in result,
         "(1, 0) is on the anti-diagonal of (0, 1): abs(1-0)==abs(0-1). "
         "Make sure BOTH diagonals are blocked."),
    )


def test_two_queens():
    placed = [(0, 1), (1, 3)]
    result = ex.safe_cells(4, placed)
    # Manually verified safe cells for N=4 with queens at (0,1) and (1,3)
    blocked = set()
    for qr, qc in placed:
        for r in range(4):
            for c in range(4):
                if c == qc or abs(r - qr) == abs(c - qc):
                    blocked.add((r, c))
    expected = {(r, c) for r in range(4) for c in range(4)} - blocked
    diagnose(
        result == expected,
        f"Expected {expected}, got {result}.",
        (lambda: len(result) > len(expected),
         "Too many safe cells — some attacked squares are not being removed."),
        (lambda: len(result) < len(expected),
         "Too few safe cells — some valid squares are being incorrectly blocked."),
    )


def test_fully_blocked():
    # 3 queens in N=3 such that no cell is safe
    placed = [(0, 0), (1, 2), (2, 1)]
    result = ex.safe_cells(3, placed)
    diagnose(
        len(result) == 0,
        f"All cells should be blocked, but got {len(result)} safe cells: {result}.",
        (lambda: len(result) > 0,
         "Every cell on a 3×3 board is attacked by at least one of the three "
         "queens — the result should be an empty set."),
    )
