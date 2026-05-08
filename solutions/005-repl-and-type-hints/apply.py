"""Rung 5: Apply — write the type hints for a function whose body is given.

Solo (rung 4) had you implement a typed `mean`. The annotations were
provided; you only had to honor them. This rung flips it: the body is
provided, you write the annotations.

Below is `chunk`: split a list into smaller fixed-size lists. The
implementation works correctly. The signature has NO annotations.

Your job: add type annotations to `items`, `size`, and the return,
then run the file. The asserts don't check behavior (it already works)
— they check via `inspect.signature` that the annotations you added
match what the docstring promises.

Concept (the day's NEW one): type hints aren't decoration. They are a
*contract* with the reader. The signature alone tells someone whether
they can pass any iterable or only a list, what gets returned, what
constraints `size` carries. You read that contract by reading the
annotations.

Run it:
    uv run python apply.py
"""
from __future__ import annotations

import inspect
from typing import get_type_hints


# TODO: add type annotations to `items`, `size`, and the return.
# The docstring tells you the shapes — items is a list of any single
# type, size is a positive int, and the return is a list of lists.
def chunk(items, size):
    """Split `items` into a list of lists, each of length `size` (last may be shorter).

    items: a list of items of any single type.
    size: a positive integer.
    returns: a list whose elements are lists matching the input element type.
    """
    return [items[i:i + size] for i in range(0, len(items), size)]


def main() -> None:
    # Behavior — already correct; included so you can see the function works.
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([], 3) == []
    assert chunk(["a", "b", "c", "d"], 1) == [["a"], ["b"], ["c"], ["d"]]

    # Annotation contract — what your hints need to say.
    sig = inspect.signature(chunk)

    assert sig.parameters["items"].annotation is not inspect.Parameter.empty, (
        "Add a type annotation to `items` (e.g. `items: list[int]`)."
    )
    assert sig.parameters["size"].annotation is not inspect.Parameter.empty, (
        "Add a type annotation to `size` (e.g. `size: int`)."
    )
    assert sig.return_annotation is not inspect.Parameter.empty, (
        "Add a return annotation to `chunk` (e.g. `-> list[list[int]]`)."
    )

    # Specifically: size must be int; return type should be a list-of-list shape.
    hints = get_type_hints(chunk)
    assert hints.get("size") is int, (
        f"`size` should be annotated as `int`, got {hints.get('size')!r}. "
        "The docstring says 'positive integer'."
    )
    return_hint = hints.get("return")
    assert return_hint is not None, "Return annotation didn't resolve."
    assert "list" in str(return_hint).lower(), (
        f"Return type doesn't look like a list-of-lists: {return_hint!r}. "
        "The docstring says 'a list whose elements are lists'."
    )

    print("✓ Annotations added — signature now reads as a contract.")
    print(f"  signature: {sig}")
    print(f"  resolved hints: {hints}")


if __name__ == "__main__":
    main()
