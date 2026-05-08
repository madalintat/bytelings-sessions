"""Rung 2: Fluency drill — solved version.

safe_cells builds the full N×N grid then removes any cell attacked by
a placed queen. A cell (r, c) is attacked when it shares a column
(c == qc) or a diagonal (abs(r-qr) == abs(c-qc)) with queen (qr, qc).
"""


def safe_cells(n: int, placed: list[tuple[int, int]]) -> set[tuple[int, int]]:
    # Start with every cell on the board
    cells = {(r, c) for r in range(n) for c in range(n)}
    for qr, qc in placed:
        # Remove every cell attacked by this queen
        cells -= {
            (r, c)
            for r in range(n)
            for c in range(n)
            if c == qc or abs(r - qr) == abs(c - qc)
        }
    return cells
