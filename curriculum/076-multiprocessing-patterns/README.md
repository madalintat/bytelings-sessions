---
day: day-076-multiprocessing-patterns
phase: phase-3-quality-production
module: module-15-concurrency-in-practice
style: build-it
---
# Day 76 — Build a worker pool (because pretend you don't have one)

You have a CPU-bound function and 8 cores. The job: run that function
on a million inputs, as fast as possible. Today, you build the
mental model from the ground up — what a worker pool *is*, and the
two patterns that handle 95% of real cases.

## What a pool is, plumbing-first

A worker pool is just three things:

1. A **queue of inputs** the main process pushes into.
2. A bunch of **worker processes** that pull inputs, compute, push
   results to a result queue.
3. A **collector** in the main process that reads results back, in
   order or out.

You can build this by hand with `multiprocessing.Process` and
`Queue`. You almost never should — `concurrent.futures.ProcessPoolExecutor`
or `multiprocessing.Pool` do this for you, with reasonable defaults.
But knowing what's underneath makes the failure modes obvious.

## Pattern 1: Map (embarrassingly parallel)

The work for each input is independent. You don't care about order
of execution. You just want all the results.

```python
from concurrent.futures import ProcessPoolExecutor

def hash_one(s: str) -> str:
    import hashlib
    return hashlib.sha256(s.encode()).hexdigest()

with ProcessPoolExecutor() as pool:
    results = list(pool.map(hash_one, inputs))
```

`pool.map` returns results in input order. With `chunksize=N`, it
batches N inputs per worker call, which slashes the
serialize-send-receive overhead per item — the difference between 2x
and 8x speedup on small fast tasks. For tasks > ~1ms, the default
chunksize is fine.

## Pattern 2: Producer/Consumer

Workers feed each other. Stage 1 reads files, stage 2 parses, stage 3
writes summaries. Each stage is its own pool, connected by a queue.

```python
from multiprocessing import Process, Queue

def parser(in_q, out_q):
    while True:
        chunk = in_q.get()
        if chunk is None:
            out_q.put(None)
            return
        out_q.put(parse(chunk))
```

The `None` sentinel is the canonical "no more work" signal — the
worker shuts down on receiving it. You build a small graph of
processes and queues. Useful when stages have very different speeds
(reader fast, parser slow), so each can scale independently.

## The pickle wall

When you submit work to a process pool, the function and its
arguments are pickled and shipped across a pipe to a worker. Three
things that bite people:

1. **Lambdas don't pickle.** Top-level functions only. (`pool.map(lambda x: x*2, items)` raises a cryptic error.)
2. **Big args are slow.** Sending a 1 GB DataFrame to each worker
   costs 1 GB of serialization per call. Use shared memory (`multiprocessing.shared_memory`) or restructure to send less.
3. **Class instances need to be importable.** A `MyHelper` defined in
   `__main__` of a script may fail to unpickle in workers. Move it to
   a module.

## Order, fairness, and timeouts

- `pool.map` preserves input order; `as_completed` doesn't.
- Workers process inputs in queue order; "fairness" across long
  running and short tasks is the OS scheduler's job, not yours.
- Always pass a `timeout` to `future.result()` in production — a
  stuck worker shouldn't take down the pool.

## When to skip the pool

Skip if:

- Each task takes <1 ms. Pool overhead eats the win.
- You only have a couple of tasks. Just call them.
- The function is a pure computation on a small input — try Numba
  or NumPy vectorization first.

## Now: open `fluency.py`

A `pool.map` call with a non-pickleable lambda. Refactor it to a
top-level function so the pool can ship it to workers.
