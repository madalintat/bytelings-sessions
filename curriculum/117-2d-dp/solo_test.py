"""HIDDEN tests for rung 4 — do not peek before solving solo.py."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_4"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "solo.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _valid_solution(sol: list[int]) -> bool:
    n = len(sol)
    for i in range(n):
        for j in range(i + 1, n):
            if sol[i] == sol[j] or abs(i - j) == abs(sol[i] - sol[j]):
                return False
    return True


def test_n1():
    assert ex.n_queens(1) == [[0]]


def test_n2_empty():
    assert ex.n_queens(2) == []


def test_n3_empty():
    assert ex.n_queens(3) == []


def test_n4_count():
    assert len(ex.n_queens(4)) == 2


def test_n4_all_valid():
    for sol in ex.n_queens(4):
        assert _valid_solution(sol), f"Invalid solution: {sol}"


def test_n5_count():
    assert len(ex.n_queens(5)) == 10


def test_n6_count():
    assert len(ex.n_queens(6)) == 4


def test_n8_count():
    assert len(ex.n_queens(8)) == 92


def test_n8_all_valid():
    for sol in ex.n_queens(8):
        assert _valid_solution(sol), f"Invalid solution: {sol}"
