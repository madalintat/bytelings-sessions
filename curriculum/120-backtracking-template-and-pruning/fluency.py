"""Rung 2: Fluency drill — fix the missing undo.

Topic: backtracking template, the apply / undo symmetry.

`subsets` should return all subsets of `arr` (each as a list). It's
missing the UNDO step on `partial`, so subtrees see polluted state
from earlier branches and the output is wrong.
"""


def subsets(arr: list) -> list[list]:
    out = []
    partial = []

    def backtrack(i: int):
        if i == len(arr):
            out.append(partial[:])    # snapshot
            return
        # choice 1: include arr[i]
        partial.append(arr[i])
        backtrack(i + 1)
        # TODO: undo the append before exploring the "exclude" branch
        # choice 2: exclude arr[i]
        backtrack(i + 1)

    backtrack(0)
    return out
