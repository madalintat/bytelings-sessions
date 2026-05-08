---
day: day-101-recursion-vs-iteration
phase: phase-5-algorithms
module: module-20-recursion
style: compare
---
# Day 101 — Two ways to add up a list. Pick one.

Here are two functions that compute the same answer.

```python
# Way A — iterative
def total_iter(nums):
    s = 0
    for n in nums:
        s += n
    return s

# Way B — recursive
def total_rec(nums):
    if not nums:
        return 0
    return nums[0] + total_rec(nums[1:])
```

Both return `total([1, 2, 3]) == 6`. So which do you reach for?

## When iteration wins

For a flat list of numbers, the iterative version is **strictly better**:

- **No stack overhead.** The recursive version pushes a new frame for
  every element. On a 10,000-element list, that's 10,000 frames — and
  Python's default recursion limit is 1,000. You'll crash.
- **`nums[1:]` allocates a new list each call.** That makes the
  recursive version O(n²) memory, not O(n). The iterative version is
  O(1) extra memory.
- **It reads in one direction.** Anyone can trace a `for` loop.
  Recursion makes you build a mental tree.

For flat data with a "step forward one item" pattern, iteration is the
clearer, faster, safer tool. Don't get fancy.

## When recursion wins

But iteration loses badly the moment data gets **branching** or the
**depth is unknown**.

```python
# Walk a directory tree — recursion is the natural shape
def walk(folder):
    for entry in folder:
        if is_file(entry):
            yield entry
        else:
            yield from walk(entry)   # recurse into subfolder
```

Try writing that with a `for` loop alone. You can — but you end up
maintaining a stack yourself (an explicit `to_visit` list), and the
"loop" is really a "manual stack of folders to process." At that
point, you've reinvented recursion. Worse.

## The decision rule

Reach for **iteration** when:
- Data is flat (a list, a string, a range).
- You move forward one step at a time.
- The bound is roughly known.

Reach for **recursion** when:
- Data is tree- or graph-shaped (each node may contain more nodes).
- The depth is data-dependent — you don't know how deep until you walk.
- The problem is *naturally* expressed as "solve smaller, combine."

## A subtle middle case: tail recursion

Some languages optimize tail-recursive functions into loops
automatically. **Python does not.** A function that "just looks like a
loop with extra steps" gets no special treatment — it pays the full
stack cost. So in Python, if a recursion is purely tail-shaped, you'd
rewrite it as a loop. (We'll see this concretely in tomorrow's
detective episode.)

## Now: open `fluency.py`

Two functions; one is best as iteration, one is best as recursion.
Both are written the wrong way. Swap each over.
