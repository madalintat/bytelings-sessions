"""Rung 2: Fluency drill — mark the safe cells on an N-queens board.

Topic: backtracking — understanding attack patterns before writing the search.

Pattern: P-27 (dfs-with-explicit-stack)

Given an N×N board with some queens already placed, figure out which
(row, col) positions are still safe for a NEW queen.

A cell (r, c) is unsafe if any placed queen (qr, qc) satisfies:
  - same column: c == qc
  - same diagonal: abs(r - qr) == abs(c - qc)

(Rows are never shared in the backtracking loop, so row conflicts are
 handled by the recursion structure — not by this function.)

>>> safe_cells(4, [])
{(0,0),(0,1),(0,2),(0,3),(1,0),...}   # all 16 cells

>>> safe_cells(4, [(0, 1), (1, 3)])
# queen at row 0, col 1 and queen at row 1, col 3 — see README trace
"""


def safe_cells(n: int, placed: list[tuple[int, int]]) -> set[tuple[int, int]]:
    """Return all (row, col) positions that are safe given the placed queens.

    Args:
        n:      board size (N×N)
        placed: list of (row, col) tuples for queens already on the board

    Returns:
        Set of (row, col) tuples where a new queen would not attack any
        of the placed queens. All cells of the board (0 <= r, c < n) that
        are not attacked are included.
    """
    # TODO: build the full set of cells and remove those attacked by any queen.
    # A cell (r, c) is attacked if any placed queen (qr, qc) has:
    #   c == qc   (same column)
    #   abs(r - qr) == abs(c - qc)   (same diagonal OR anti-diagonal)
    raise NotImplementedError
