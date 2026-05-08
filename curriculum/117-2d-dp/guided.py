"""Rung 3: Guided — implement is_safe for N-queens.

Topic: backtracking, the safety predicate.

Pattern: P-27 (dfs-with-explicit-stack)

The backtracking recursion is provided below as a sketch. Your only
job is to fill in `is_safe`. Once it is correct, `n_queens_guided`
returns the right answers.

`cols` is a list where `cols[r]` is the column of the queen on row r.
`len(cols)` equals the number of queens placed so far.

To place a queen at (row, col), we check whether any existing queen
at row r (0 <= r < len(cols)) with column cols[r] attacks (row, col):
  - same column:   cols[r] == col
  - same diagonal: abs(row - r) == abs(col - cols[r])

>>> n_queens_guided(4)   # 2 solutions
[[1, 3, 0, 2], [2, 0, 3, 1]]
"""


def is_safe(row: int, col: int, cols: list[int]) -> bool:
    """Return True if placing a queen at (row, col) is safe given cols.

    Args:
        row:  the row we want to place a queen in (== len(cols))
        col:  the column we are considering
        cols: cols[r] = column of the queen already on row r

    Returns:
        True iff no queen in cols attacks (row, col).
    """
    # TODO: iterate over placed queens and return False if any attacks (row, col).
    # Check: same column (cols[r] == col)
    #   and: same diagonal (abs(row - r) == abs(col - cols[r]))
    raise NotImplementedError


# --- provided recursion skeleton (do not edit) ---

def n_queens_guided(n: int) -> list[list[int]]:
    """Return all N-queens solutions using is_safe above.

    Each solution is a list of N column indices, one per row.
    """
    solutions: list[list[int]] = []
    cols: list[int] = []

    def solve(row: int) -> None:
        if row == n:
            solutions.append(cols.copy())
            return
        for col in range(n):
            if is_safe(row, col, cols):
                cols.append(col)
                solve(row + 1)
                cols.pop()  # backtrack

    solve(0)
    return solutions
