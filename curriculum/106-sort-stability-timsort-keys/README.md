---
day: day-106-sort-stability-timsort-keys
phase: phase-5-algorithms
module: module-21-searching-sorting
style: compare
---
# Day 106 — Two ways to "sort by date, then by user"

You have a list of events. You want them sorted by user, and within
each user, by timestamp. Two approaches.

## Way A — composite key

```python
events.sort(key=lambda e: (e.user, e.timestamp))
```

Build a tuple key. Tuples compare lexicographically: user first, then
timestamp as tiebreaker. One sort. O(n log n) total.

## Way B — sort by timestamp first, then by user

```python
events.sort(key=lambda e: e.timestamp)
events.sort(key=lambda e: e.user)
```

Sort the list twice. The *second* sort wins on the primary field, but
within ties (same user), the order from the *first* sort is
preserved. The order looks the same as Way A.

That second behavior — equal-keyed elements keeping their relative
order — is **stability**. Without it, Way B would scramble the
timestamp ordering inside each user.

## Which is "right"?

Both work. Way A is what you'd do if you can express all your sort
criteria in one tuple. Way B is what you do when criteria come from
different places (different sort directions, different functions, or
sorts done at different times in your code). They're both idiomatic
Python because **`list.sort()` and `sorted()` are stable**.

Python's sort algorithm — **Timsort** — was invented by Tim Peters in
2002 specifically for `sorted()`. It's now used in Java, Android,
JavaScript engines, Rust, and Swift. It's stable, O(n log n) worst
case, and *near-linear on partially-sorted data* (which real-world
data usually is).

## A quick mental model of Timsort

1. **Find existing runs** of sorted data in the input (forward or
   reversed; reversed gets flipped).
2. **Use insertion sort to extend tiny runs** up to a minimum length
   (~32). Insertion sort wins on small arrays.
3. **Merge runs in a clever order** that minimizes worst-case work.

You will never hand-roll Timsort. But knowing it exists changes how
you write code: you can stop pre-sorting "to help the sort." Timsort
already handles partial order. Pass your data straight in.

## The `key` parameter — your primary sort tool

Don't write a comparator function in modern Python. Use `key`.

```python
people.sort(key=lambda p: p.age)                  # by age
people.sort(key=lambda p: -p.age)                 # by age descending
people.sort(key=lambda p: (p.lastname, p.age))    # last name, then age
people.sort(key=str.lower)                        # case-insensitive
```

`key` is called once per element, then the results are compared. So
even a complex key function is fine — it doesn't run O(n²) times like
a comparator would.

## WHEN to think about stability

- **Multi-pass sorting** (Way B above): only stable sort works.
- **Sorting records where some columns aren't in the key**: stable
  sort preserves the original order of those columns.
- **External sorts and parallel sorts**: stability is harder to
  preserve in distributed systems; check what you've got.

## Now: open `02_fluency.py`

Two attempts at "sort by name, then by age." One uses a tuple key but
gets the order wrong; one uses two passes but loses stability. Fix
each.
