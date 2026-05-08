---
day: day-104-bubble-insertion-selection
phase: phase-5-algorithms
module: module-21-searching-sorting
style: tour
---
# Day 104 — A guided tour of three "bad" sorts

You will never use bubble sort in production. You'll use Python's
built-in `sorted()` (Timsort, ~O(n log n)). So why learn the slow ones?

Because they're the fastest path to *feeling* what sorting is. They
each illustrate one idea so cleanly you'll recognize the same idea in
real algorithms (and elsewhere — selection sort's pattern shows up in
every "find the next minimum" loop you'll ever write).

## Stop 1 — Bubble sort

```python
def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

Walk the list. Adjacent items in the wrong order swap. After one full
pass, the largest item has "bubbled" to the end. Repeat n times. O(n²).

The idea: **each pass moves one element to its final position.** Slow,
but a clean lens for understanding "why does sorting take more than
linear time?"

## Stop 2 — Selection sort

```python
def selection(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

Find the smallest. Swap to the front. Now look at the rest, find
*its* smallest, swap. Also O(n²). One swap per pass, which is nice
if writes are expensive (think: sorting on flash storage, where
writes wear the chip).

The idea: **build the sorted prefix one element at a time, by picking
the next minimum.** This is the shape of a *priority queue* (heaps,
Module 19). When you replace "scan to find the min" with "pop the
min from a heap," selection sort becomes heapsort and is now O(n log n).

## Stop 3 — Insertion sort

```python
def insertion(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cur:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cur
    return arr
```

Take each item and slide it backward into its correct spot among the
already-sorted ones to its left. Worst case O(n²), but **near-O(n) on
nearly-sorted input**. This last property is why it's used in real
production sorts (Timsort uses insertion sort on small chunks).

## WHEN any of these win

- **Tiny arrays (< 50 elements).** The overhead of a fancy sort
  outweighs the n² cost. Insertion sort is genuinely fastest here —
  Python's Timsort uses it under the hood for short runs.
- **Nearly-sorted data.** Insertion sort's best case is O(n). If
  your data only has a few elements out of place, beats Timsort cold-
  start.
- **Streaming data, one element at a time.** Insertion sort is
  *online* — you can grow the sorted prefix as data arrives.

For everything else: `sorted()`. The day's not for production code,
it's for grokking the moves.

## Now: open `fluency.py`

A swap is wrong. Find it.
