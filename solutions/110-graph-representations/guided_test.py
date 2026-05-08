"""Tests for rung 3."""
import importlib.util
from pathlib import Path

_HERE = Path(__file__).parent
_NAME = f"_{_HERE.name}_rung_3"
_spec = importlib.util.spec_from_file_location(_NAME, _HERE / "guided.py")
ex = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ex)


def _norm(adj):
    return {k: sorted(v) for k, v in adj.items()}


def test_m_to_a_basic():
    m = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    assert _norm(ex.matrix_to_adj(m)) == {0: [1], 1: [2], 2: [0]}


def test_m_to_a_empty_rows():
    m = [[0, 1], [0, 0]]
    out = _norm(ex.matrix_to_adj(m))
    assert out == {0: [1], 1: []}


def test_m_to_a_self_loop():
    m = [[1, 0], [0, 0]]
    out = _norm(ex.matrix_to_adj(m))
    assert out == {0: [0], 1: []}


def test_a_to_m_basic():
    adj = {0: [1], 1: [2], 2: [0]}
    assert ex.adj_to_matrix(adj, 3) == [[0, 1, 0], [0, 0, 1], [1, 0, 0]]


def test_a_to_m_empty():
    assert ex.adj_to_matrix({}, 2) == [[0, 0], [0, 0]]


def test_a_to_m_partial():
    adj = {0: [2]}
    assert ex.adj_to_matrix(adj, 3) == [[0, 0, 1], [0, 0, 0], [0, 0, 0]]


def test_round_trip():
    m = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    a = ex.matrix_to_adj(m)
    assert ex.adj_to_matrix(a, 3) == m
