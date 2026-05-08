"""Rung 3: Guided implement.

Topic: classify workloads — async vs threads vs neither

For each (kind, blocking_call) pair, return one of:
    "async"   — I/O-bound; the event loop is the right tool
    "threads" — CPU-bound; async won't help, threads/processes will
    "neither" — already non-blocking; no concurrency tool needed

The kind values you'll see in the tests:
    - "http"        : waiting on a network response
    - "sleep"        : asyncio.sleep / time.sleep
    - "disk_read"    : reading bytes from disk
    - "hash_4gb"     : hashing a multi-GB file in pure Python
    - "matrix_mul"   : multiplying two large NumPy matrices
    - "in_memory"    : a pure-Python lookup in a dict
"""


def best_tool(kind: str) -> str:
    """Return 'async', 'threads', or 'neither'.

    Use the categories described above. Anything CPU-heavy returns
    'threads'. Anything that waits on I/O returns 'async'. Pure
    in-memory work is 'neither'.
    """
    # TODO: implement. A small dict or if/elif chain is fine.
    raise NotImplementedError
