"""Rung 2: Fluency drill — read this function, then describe it.

Topic: building the reading habit.

The function below has no docstring. Read it, run the tests to see
its behavior, then ADD a short docstring (one sentence is fine) that
correctly describes what it does. The tests check that the docstring
exists and contains the right keyword.
"""


def mystery(items: list[int]) -> list[int]:
    # TODO: add a docstring describing what this returns.
    # Hint: it removes consecutive duplicates only.
    out: list[int] = []
    for x in items:
        if not out or out[-1] != x:
            out.append(x)
    return out
