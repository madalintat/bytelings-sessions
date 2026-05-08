"""Rung 5: Apply — solved version (type hints filled in).

The skeleton from curriculum/005-repl-and-type-hints/apply.py is the
same; the difference is the three annotations on `chunk` are now
filled in.

The most idiomatic typing uses TypeVar so the relationship "input
element type T → output is list[list[T]]" is captured. A simpler
non-generic annotation (e.g. `list[int]` everywhere) would also
satisfy the asserts in main(), so both are correct answers — but
the TypeVar version is what a senior engineer would write.
"""
from __future__ import annotations

import inspect
from typing import TypeVar, get_type_hints

T = TypeVar("T")


def chunk(items: list[T], size: int) -> list[list[T]]:
    """Split `items` into a list of lists, each of length `size` (last may be shorter)."""
    return [items[i:i + size] for i in range(0, len(items), size)]


def main() -> None:
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk([], 3) == []
    assert chunk(["a", "b", "c", "d"], 1) == [["a"], ["b"], ["c"], ["d"]]

    sig = inspect.signature(chunk)
    assert sig.parameters["items"].annotation is not inspect.Parameter.empty
    assert sig.parameters["size"].annotation is not inspect.Parameter.empty
    assert sig.return_annotation is not inspect.Parameter.empty

    hints = get_type_hints(chunk)
    assert hints.get("size") is int
    assert "list" in str(hints.get("return")).lower()

    print("✓ Annotations added — signature now reads as a contract.")
    print(f"  signature: {sig}")
    print(f"  resolved hints: {hints}")


if __name__ == "__main__":
    main()
