---
day: day-015-list-methods-and-mutation
phase: phase-1-python-core
module: module-03-lists-and-bigo
style: detective
---
# Day 15 — Why `sort()` returned `None`

A teammate is debugging. Her function returns `None` instead of a
sorted list. Here's the suspect:

```python
def sorted_user_ids(users):
    ids = [u["id"] for u in users]
    return ids.sort()        # ← bug
```

She ran it. Got `None`. She blamed her data. Spent 20 minutes on the
wrong file.

## The clue

Python list methods come in two flavors. **In-place** methods mutate
the list and return `None`:

| Method | What | Returns |
|---|---|---|
| `lst.sort()` | sort in place | None |
| `lst.reverse()` | reverse in place | None |
| `lst.append(x)` | add to end | None |
| `lst.extend(other)` | concat in place | None |
| `lst.insert(i, x)` | insert at i | None |
| `lst.remove(x)` | first matching value | None |
| `lst.clear()` | empty the list | None |

**Returns-a-new-thing** functions/methods leave the original alone:

| Call | What | Returns |
|---|---|---|
| `sorted(lst)` | sorted copy | new list |
| `reversed(lst)` | reverse iterator | iterator (wrap in list()) |
| `lst + other` | concat | new list |
| `lst.copy()` | shallow copy | new list |
| `lst.pop()` | remove last | the removed item |
| `lst.pop(0)` | remove first | the removed item |
| `lst.index(x)` | position | int (raises if missing) |
| `lst.count(x)` | matches | int |

The fix to her bug:

```python
return sorted(ids)             # use the function (new list)
# OR
ids.sort()                     # mutate
return ids                     # then return the list
```

## A second case: mutation while iterating

```python
items = [1, 2, 3, 4]
for x in items:
    if x % 2 == 0:
        items.remove(x)     # bug
# items is [1, 3] (lucky) or items is [1, 3, 4] (unlucky, depending)
```

Removing while iterating skips elements because the index advances
even though the list shrunk. The pythonic answers:

```python
items = [x for x in items if x % 2 != 0]   # new list (preferred)
items[:] = [x for x in items if x % 2 != 0] # mutate in place if you must
```

## A third case: the default-argument trap (preview)

```python
def append_to(x, lst=[]):
    lst.append(x)
    return lst
```

Defaults are evaluated **once**, when the function is defined — so the
list is shared across calls. This is the most-loved Python interview
gotcha and we'll cover it on Day 24. Today's lesson: respect the
mutation/return distinction.

## Verdict

Sort returned `None`. The detective's rule: **if a method's name is a
verb and the verb describes *changing* the list, it returns `None`.**
Use `sorted`, `reversed`, comprehensions, or `+` for new lists.

## Now: open `fluency.py`

Three small bugs around mutation vs return. Fix each.
