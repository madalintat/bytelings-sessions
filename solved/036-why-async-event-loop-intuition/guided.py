"""Rung 3: Guided — solved version.

The dispatch dict makes the classification explicit and avoids a chain
of if/elif. CPU-heavy work ("hash_4gb", "matrix_mul") belongs to
threads/processes; all I/O-waiting work ("http", "sleep", "disk_read")
belongs to async; pure in-memory work ("in_memory") needs no
concurrency.
"""

_TOOL = {
    "http":       "async",
    "sleep":      "async",
    "disk_read":  "async",
    "hash_4gb":   "threads",
    "matrix_mul": "threads",
    "in_memory":  "neither",
}


def best_tool(kind: str) -> str:
    """Return 'async', 'threads', or 'neither'."""
    return _TOOL[kind]
