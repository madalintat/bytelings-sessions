"""CLI — adds `reset`, `recent`, and `list --sort` for day 4."""
from __future__ import annotations
from datetime import date, timedelta

import click

from . import storage
from .core import sort_key_streak


@click.group()
@click.version_option("0.1.0", package_name="habit")
def main() -> None:
    """Track tiny daily habits."""


@main.command(name="list")
@click.option("--sort", type=click.Choice(["name", "streak"]), default="name",
              help="Sort order.")
def list_cmd(sort: str) -> None:
    """List all habits and their streaks."""
    path = storage.default_data_path()
    habits = storage.load(path)
    if not habits:
        click.echo("(no habits yet — try `habit done <name>`)")
        return
    today = date.today()
    if sort == "streak":
        ordered = sorted(habits.values(), key=sort_key_streak(today))
    else:
        ordered = sorted(habits.values(), key=lambda h: h.name)
    for habit in ordered:
        click.echo(f"{habit.name}: {habit.streak(today)}-day streak")


@main.command()
@click.argument("name")
def done(name: str) -> None:
    """Mark <name> done for today."""
    path = storage.default_data_path()
    habits = storage.load(path)
    today = date.today()
    habit = storage.mark_done(habits, name, today)
    storage.save(path, habits)
    click.echo(f"recorded {name} on {today.isoformat()} ({habit.streak(today)}-day streak)")


@main.command()
@click.argument("name")
@click.option("--yes", is_flag=True, help="Skip confirmation prompt.")
def reset(name: str, yes: bool) -> None:
    """Wipe the log for <name>."""
    path = storage.default_data_path()
    habits = storage.load(path)
    if name not in habits:
        click.echo(f"no habit named {name!r}", err=True)
        raise SystemExit(1)
    if not yes and not click.confirm(f"Really wipe history for {name!r}?"):
        click.echo("aborted")
        return
    habits[name].clear()
    storage.save(path, habits)
    click.echo(f"reset {name}")


@main.command()
@click.option("--days", default=14, show_default=True,
              help="How many days of history to show.")
def recent(days: int) -> None:
    """Show the last N days as a tiny grid."""
    path = storage.default_data_path()
    habits = storage.load(path)
    if not habits:
        click.echo("(no habits yet)")
        return
    today = date.today()
    window = [today - timedelta(days=days - 1 - i) for i in range(days)]
    width = max(len(name) for name in habits) + 2
    for name in sorted(habits):
        cells = " ".join("X" if d in habits[name].log else "." for d in window)
        click.echo(f"{name.ljust(width)}{cells}")
    legend = " ".join(d.strftime("%a")[0] for d in window)
    click.echo(f"{' ' * width}{legend}")
