"""Rung 4: Solo — full N-queens.

Topic: backtracking, enumerate all solutions.

Pattern: P-27 (dfs-with-explicit-stack)

Implement `n_queens(n)` returning ALL solutions to the N-queens problem.
Each solution is a list of N column indices, one per row: solution[r]
is the column of the queen on row r.

>>> n_queens(1)
[[0]]
>>> len(n_queens(4))
2
>>> len(n_queens(8))
92

Hints:
- Copy the backtracking template from the README:
    def solve(state): complete? record. else: for choice: apply/recurse/undo.
- State: a list `cols` of column indices placed so far.
- is_complete: len(cols) == n.
- legal_next_choices: columns 0..n-1 that are safe at row len(cols).
- undo: cols.pop().

Tests in solo_test.py are HIDDEN — do not peek before solving.
"""


def n_queens(n: int) -> list[list[int]]:
    """Return all N-queens solutions as lists of column-per-row.

    Each inner list has length n; inner_list[r] = column of queen in row r.
    """
    raise NotImplementedError
