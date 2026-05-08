"""Rung 4: Solo — solved version.

`naturals` is an infinite generator: a `while True` loop with a yield.
The `yield` suspends execution and hands a value to the caller; the
next `next()` call resumes right after the yield.

`take_while` wraps any source: it pulls one item at a time and yields
it only while the predicate holds. The moment the predicate fails it
returns, which closes the generator without exhausting the source —
crucial for infinite sources.
"""


def naturals():
    n = 1
    while True:
        yield n
        n += 1


def take_while(predicate, source):
    for item in source:
        if not predicate(item):
            return
        yield item
