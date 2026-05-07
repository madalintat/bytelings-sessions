"""All rich-based output for the swe runner."""
from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


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
    table = Table(show_header=True, header_style="bold")
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
    console.print(table)


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
