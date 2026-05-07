---
day: day-050-iter-len-contains-dunders
phase: phase-2-pythonic-tools
module: module-09-classes-dunders-context-managers
style: build-it
---
# Day 50 — Pretend `len()`, `in`, and `for` don't work on your object. Make them.

You build a class to model a deck of cards, a shopping cart, a playlist
— anything collection-shaped. You want it to feel native:

```python
deck = Deck()
len(deck)            # works
"king of hearts" in deck   # works
for card in deck:    # works
    print(card)
```

You don't get any of that for free. But you can opt in by writing three
small dunders. Each one is the hook Python uses for one operator.

## `__len__`: what `len()` calls

```python
class Cart:
    def __init__(self):
        self.items = []
    def __len__(self):
        return len(self.items)
```

`len(cart)` now works. Bonus: `if cart:` also works — when an object
defines `__len__`, Python uses it for truthiness too. Empty cart → falsy.

The contract: return a non-negative integer.

## `__contains__`: what `in` calls

```python
class Cart:
    def __contains__(self, sku: str) -> bool:
        return any(item.sku == sku for item in self.items)
```

`"abc-123" in cart` now works. The contract: return a bool.

Without `__contains__`, Python falls back to iterating with
`__iter__` and checking each element with `==`. So if you implement
`__iter__`, `in` already works in O(n). You only override
`__contains__` when you can do it faster (a set lookup, an index, etc.).

## `__iter__`: what `for ... in` calls

You saw the iterator protocol on Day 34. Reminder:

```python
class Cart:
    def __iter__(self):
        return iter(self.items)
```

The simplest way: delegate to whatever underlying collection you
already have. `iter(self.items)` returns a fresh iterator each time,
so you can loop the cart multiple times.

If you want lazy or computed iteration, write a generator:

```python
def __iter__(self):
    for item in self.items:
        if item.in_stock:
            yield item
```

## Three more worth knowing now

- `__getitem__(self, key)` — what `cart[0]` and `cart["sku"]` call.
  If you define this *and not* `__iter__`, Python will iterate by
  calling `cart[0]`, `cart[1]`, ... until `IndexError`. (This is how
  iteration worked before iterators existed.)
- `__bool__(self)` — what `bool(x)` and `if x:` call when `__len__`
  isn't defined. Returns True/False explicitly.
- `__str__(self)` — what `str(x)` and `print(x)` call. Defaults to
  `__repr__`.

## The pattern

When you build a class that holds a collection, ask: do users want to
`len(it)`, `for ... in it`, or `x in it`? Each answer is one tiny
method. Adding them turns your class from "a thing with a method
called `.size()`" into "a Pythonic container."

## Now: open `02_fluency.py`

A `Bag` class that stores items but doesn't speak the container protocol.
