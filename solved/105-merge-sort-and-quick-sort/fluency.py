"""Rung 2: Fluency — solved version.

When one list is exhausted the loop exits and the remaining elements
of the other list are silently dropped. Append them with slice
extension: `out += a[i:]` and `out += b[j:]`. Since one index is at
the end of its list, one of those slices will be empty — the correct
one appends its remainder.
"""


def merge(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list in O(n)."""
    out = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out += a[i:]
    out += b[j:]
    return out
