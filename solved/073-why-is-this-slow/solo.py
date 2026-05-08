"""Rung 4: Solo implement — solved version.

Single-pass set-based approach: for each x, check if (target - x)
is already in `seen`. If so, record the pair (smaller first). Then
add x to `seen`. Dedupe and sort the result.
"""


def find_pairs(xs: list[int], target: int) -> list[tuple[int, int]]:
    seen: set[int] = set()
    pairs: set[tuple[int, int]] = set()
    for x in xs:
        complement = target - x
        if complement in seen:
            pair = (min(x, complement), max(x, complement))
            pairs.add(pair)
        seen.add(x)
    return sorted(pairs)
