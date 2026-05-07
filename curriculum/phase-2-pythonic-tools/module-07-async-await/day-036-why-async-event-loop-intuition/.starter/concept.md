---
day: day-036-why-async-event-loop-intuition
phase: phase-2-pythonic-tools
module: module-07-async-await
style: metaphor
---
# Day 36 — The chef and the oven

Picture a small restaurant kitchen. There's one chef. There are four
ovens, each with its own timer. A ticket comes in:

> "Three roast chickens. Forty minutes each."

A bad chef puts in the first chicken, stares at the oven for forty
minutes, takes it out, then puts in the second one, stares for forty
more minutes, then the third. Two hours total. The chef did almost no
work — they were just *waiting*.

A good chef puts all three chickens in three ovens, sets the timers,
and goes off to chop vegetables for the next ticket. When a timer
dings, they handle that oven. Forty-something minutes total. The chef
is rarely idle, but they're still only one chef.

That second chef is the **event loop**.

## What async actually buys you

In a Python program, the "ovens" are things like:

- An HTTP request waiting for a response.
- A database query waiting for a row.
- A file being read from a slow disk.
- A `sleep` waiting for time to pass.

These are I/O-bound waits. The CPU could be doing other useful work
during them, but in a synchronous program it isn't — your code is just
sitting at the call site, blocked.

`async`/`await` is Python's way of letting one thread juggle many of
these waits at once. When your code hits an `await`, it tells the event
loop: "I'm parked until this thing completes — go do something else."
The loop runs other ready tasks. When the awaited thing is done, the
loop wakes your code back up.

## What it does NOT buy you

Async is for **I/O-bound** work, not CPU-bound work. If your task is
"compute SHA-256 of a 4 GB file," async doesn't help — there's no oven
timer to wait on. The chef would just be chopping the whole time. For
that, you want threads or processes (Phase 3, Module 15).

Rule of thumb: if the speedup you want comes from things happening
*while you wait*, reach for async. If it comes from doing more work *at
the same time*, reach for threads/processes.

## Mental model for the rest of this module

- One thread. One event loop. Many `Task`s.
- A `Task` is a chicken in an oven — running, but able to pause at
  `await` points.
- `await` = "park me until this is done, give the chef some other ticket."
- `asyncio.run(coro)` = "open the kitchen, run this ticket and any tasks
  it spawns, then close up."
- `asyncio.gather(a, b, c)` = "fire all three ovens, wake me when they're
  all done."

Hold on to this picture. Every async pattern you'll see for the next
six days is a variation on it.

## Now: open `02_fluency.py`

Two predict-the-output questions about a tiny chef-and-ovens simulation.
