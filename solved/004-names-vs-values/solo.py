"""Rung 4: Solo — solved version.

The `dedupe-while-preserving-order` idiom: walk the input, track
'already seen' in a set, append only first sightings.

  seen: set = set()
  out: list = []
  for x in items:
      if x not in seen:
          seen.add(x)
          out.append(x)
  return out

Why a set? Membership test is O(1) average — without it, `x not in
out` is O(n) per iteration and the function is O(n²) overall.

Why `out = []` (not `out = items[:]`)? Returning a NEW list, not a
mutated copy of the input. The contract says "do not mutate input"
— even copying the input first violates the spirit if you then
modify the copy.

The `dict.fromkeys(items)` trick exists (`list(dict.fromkeys(items))`
also dedupes in order) and is shorter, but it's slightly less
readable for learners on Day 4. Prefer the explicit version.
"""


def unique_preserving_order(items: list) -> list:
    seen: set = set()
    out: list = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out
