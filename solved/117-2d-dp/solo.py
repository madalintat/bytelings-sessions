"""Rung 4: Solo — solved version.

Full N-queens backtracking. The is_safe check mirrors guided.py.
cols is mutated in-place and popped on backtrack — that single pop()
is the defining line of the backtracking pattern.

Pattern: P-27 (dfs-with-explicit-stack)
"""


def n_queens(n: int) -> list[list[int]]:
    solutions: list[list[int]] = []
    cols: list[int] = []  # cols[r] = column of queen on row r

    def is_safe(row: int, col: int) -> bool:
        for r, c in enumerate(cols):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def solve(row: int) -> None:
        if row == n:
            # Complete solution — record a snapshot
            solutions.append(cols.copy())
            return
        for col in range(n):
            if is_safe(row, col):
                cols.append(col)
                solve(row + 1)
                cols.pop()  # backtrack: undo the choice

    solve(0)
    return solutions
