"""Rung 3: Guided — solved version.

is_safe checks each placed queen for a column conflict (cols[r] == col)
or a diagonal conflict (abs(row - r) == abs(col - cols[r])). The abs()
handles BOTH the main diagonal and the anti-diagonal in one expression.
"""


def is_safe(row: int, col: int, cols: list[int]) -> bool:
    for r, c in enumerate(cols):
        # Same column or same diagonal (either direction)
        if c == col or abs(row - r) == abs(col - c):
            return False
    return True


# --- provided recursion (unchanged) ---

def n_queens_guided(n: int) -> list[list[int]]:
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
                cols.pop()

    solve(0)
    return solutions
