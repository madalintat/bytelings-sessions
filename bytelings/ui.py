"""All rich-based output for the bytelings runner.

Two flavors of output live here:

* Top-level helpers (`header`, `banner_pass`, …) — used by one-shot CLI
  commands (`bytelings run`, `bytelings done`, …) that print once and
  exit. Plain `console.print`, no in-place magic.
* `RunnerUI` — the watcher's persistent TUI. Owns a `rich.live.Live`
  with a `Layout` split into header / rungs / body / footer, and
  mutates the body region in place on each save. This is what makes
  the watcher feel like rustlings instead of an unbounded scroll of
  panels.
"""
from __future__ import annotations

import contextlib
import threading
from datetime import datetime
from typing import Iterable

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


# ---- one-shot helpers (used by cli.py subcommands) -------------------------


def header(title: str) -> None:
    console.print(Panel(Text(title, style="bold cyan"), border_style="cyan"))


def banner_pass(rung_label: str, hint: str = "") -> None:
    text = Text.from_markup(f"[bold green]✔ {rung_label} passed[/bold green]")
    if hint:
        text.append(f"\n\n{hint}", style="dim")
    console.print(Panel(text, border_style="green"))


def banner_fail(message: str, hint: str = "") -> None:
    text = Text.from_markup("[bold red]✘ Tests failing[/bold red]\n\n")
    text.append(message)
    if hint:
        text.append(f"\n\n{hint}", style="dim")
    console.print(Panel(text, border_style="red"))


def banner_day_complete(day_slug: str, streak: int) -> None:
    text = Text()
    text.append(f"🎉 Day complete: {day_slug}\n\n", style="bold green")
    text.append(f"🔥 Streak: {streak} day(s)", style="yellow")
    console.print(Panel(text, border_style="green"))


def rung_table(rungs, current: int, completed: list[int]) -> None:
    console.print(_build_rung_table(rungs, current, completed))


def progress_summary(
    completed: int,
    total: int,
    streak: int,
    longest_streak: int,
) -> None:
    pct = int(100 * completed / total) if total else 0
    bar_width = 30
    filled = int(bar_width * completed / total) if total else 0
    bar = "█" * filled + "░" * (bar_width - filled)
    console.print(
        f"\n[bold]Progress[/bold]: {completed}/{total} days  ({pct}%)\n"
        f"[cyan]{bar}[/cyan]\n"
        f"🔥 Current streak: {streak}    🏆 Longest: {longest_streak}\n"
    )


# ---- shared bits -----------------------------------------------------------


def _build_rung_table(rungs: Iterable, current: int, completed: list[int]) -> Table:
    table = Table(show_header=True, header_style="bold", expand=True)
    table.add_column("", width=3)
    table.add_column("Rung")
    table.add_column("Name")
    table.add_column("File")
    for r in rungs:
        if r.number in completed:
            marker = "[green]✔[/green]"
        elif r.number == current:
            marker = "[cyan]→[/cyan]"
        else:
            marker = "[dim]○[/dim]"
        table.add_row(marker, str(r.number), r.name, r.file.name)
    return table


# ---- the persistent watcher TUI -------------------------------------------


class RunnerUI:
    """Rustlings-style live TUI for the watcher.

    The terminal is split into four regions that update in place:

        ┌──────────────────────────────────────────┐
        │ header  — day-NNN — Rung N: <name>       │
        ├──────────────────────────────────────────┤
        │ rungs   — checklist of the day's 5 rungs │
        ├──────────────────────────────────────────┤
        │ body    — running… / ✔ / ✘ + run #N · ts │
        ├──────────────────────────────────────────┤
        │ footer  — key legend                     │
        └──────────────────────────────────────────┘

    Rule: never print to ``console`` while the UI is started — it'll
    fight the alt-screen Live owns. Use ``paused()`` to drop out for
    blocking input or pager-style content, then return.
    """

    _IDLE_BODY_HINT = (
        "[dim]Save the rung's file in your editor (or press [bold]r[/bold]) "
        "to run its tests.[/dim]"
    )

    _DEFAULT_FOOTER = (
        "[dim]keys: [bold]r[/bold] rerun  "
        "[bold]h[/bold] hint  [bold]l[/bold] list  "
        "[bold]c[/bold] change day  [bold]q[/bold] quit[/dim]"
    )

    def __init__(self, console: Console = console) -> None:
        self._console = console
        self._layout = Layout(name="root")
        self._layout.split_column(
            Layout(name="header", size=3),
            Layout(name="rungs", size=9),
            Layout(name="body", ratio=1, minimum_size=5),
            Layout(name="footer", size=3),
        )
        self._title = "bytelings"
        self._footer_markup = self._DEFAULT_FOOTER
        self._run_count = 0
        self._live: Live | None = None
        # Live's own lock + ours: mutations come from both the watchdog
        # observer thread (on save) and the main keystroke thread.
        self._lock = threading.Lock()

        # Seed every region so the initial frame isn't half-empty.
        self._set_header(self._title)
        self._set_rungs(_placeholder_rungs())
        self._set_body(
            Panel(
                Text.from_markup(self._IDLE_BODY_HINT),
                border_style="dim",
                title="status",
                title_align="left",
            )
        )
        self._set_footer(self._footer_markup)

    # -- lifecycle ----------------------------------------------------------

    def start(self) -> None:
        if self._live is not None:
            return
        self._live = Live(
            self._layout,
            console=self._console,
            screen=True,
            auto_refresh=False,
            redirect_stdout=False,
            redirect_stderr=False,
        )
        self._live.start(refresh=True)

    def stop(self) -> None:
        if self._live is None:
            return
        live, self._live = self._live, None
        live.stop()

    @contextlib.contextmanager
    def paused(self):
        """Drop out of the alt screen so blocking input/print is visible."""
        was_running = self._live is not None
        if was_running:
            self.stop()
        try:
            yield
        finally:
            if was_running:
                self.start()

    # -- region setters ----------------------------------------------------

    def set_title(self, title: str) -> None:
        self._title = title
        with self._lock:
            self._set_header(title)
            self._refresh()

    def set_rungs(self, rungs, current: int, completed: list[int]) -> None:
        with self._lock:
            self._set_rungs(_build_rung_table(rungs, current, completed))
            self._refresh()

    def set_footer(self, markup: str | None = None) -> None:
        markup = markup or self._DEFAULT_FOOTER
        self._footer_markup = markup
        with self._lock:
            self._set_footer(markup)
            self._refresh()

    # -- body state transitions --------------------------------------------

    def set_running(self) -> None:
        with self._lock:
            self._run_count += 1
            ts = _now()
            self._set_body(
                Panel(
                    Text.from_markup(
                        "[bold yellow]⏳ Running tests…[/bold yellow]\n\n"
                        f"[dim]Run #{self._run_count} · {ts}[/dim]"
                    ),
                    border_style="yellow",
                    title="status",
                    title_align="left",
                )
            )
            self._refresh()

    def set_pass(self, rung_label: str, hint: str = "") -> None:
        with self._lock:
            ts = _now()
            text = Text.from_markup(
                f"[bold green]✔ {rung_label} passed[/bold green]"
            )
            text.append(
                f"   Run #{self._run_count} · {ts}\n", style="dim"
            )
            if hint:
                text.append(f"\n{hint}", style="dim")
            self._set_body(
                Panel(
                    text,
                    border_style="green",
                    title="status",
                    title_align="left",
                )
            )
            self._refresh()

    def set_fail(self, message: str) -> None:
        with self._lock:
            ts = _now()
            text = Text.from_markup("[bold red]✘ Tests failing[/bold red]")
            text.append(
                f"   Run #{self._run_count} · {ts}\n\n", style="dim"
            )
            text.append(message)
            self._set_body(
                Panel(
                    text,
                    border_style="red",
                    title="status",
                    title_align="left",
                    expand=True,
                )
            )
            self._refresh()

    def set_day_complete(self, day_slug: str, streak: int) -> None:
        with self._lock:
            text = Text()
            text.append(f"🎉 Day complete: {day_slug}\n\n", style="bold green")
            text.append(f"🔥 Streak: {streak} day(s)", style="yellow")
            self._set_body(
                Panel(
                    text,
                    border_style="green",
                    title="status",
                    title_align="left",
                )
            )
            self._refresh()

    def set_message(self, markup: str, border: str = "cyan") -> None:
        with self._lock:
            self._set_body(
                Panel(
                    Text.from_markup(markup),
                    border_style=border,
                    title="status",
                    title_align="left",
                )
            )
            self._refresh()

    # -- introspection (used by tests) -------------------------------------

    @property
    def run_count(self) -> int:
        return self._run_count

    @property
    def body_renderable(self):
        return self._layout["body"].renderable

    # -- internals ---------------------------------------------------------

    def _set_header(self, title: str) -> None:
        self._layout["header"].update(
            Panel(Text(title, style="bold cyan"), border_style="cyan")
        )

    def _set_rungs(self, renderable) -> None:
        self._layout["rungs"].update(renderable)

    def _set_body(self, renderable) -> None:
        self._layout["body"].update(renderable)

    def _set_footer(self, markup: str) -> None:
        self._layout["footer"].update(
            Panel(
                Text.from_markup(markup),
                border_style="dim",
            )
        )

    def _refresh(self) -> None:
        if self._live is not None:
            self._live.refresh()


def _now() -> str:
    return datetime.now().strftime("%H:%M:%S")


def _placeholder_rungs() -> Table:
    table = Table(show_header=True, header_style="bold", expand=True)
    table.add_column("", width=3)
    table.add_column("Rung")
    table.add_column("Name")
    table.add_column("File")
    table.add_row("[dim]…[/dim]", "—", "loading rungs…", "")
    return table
