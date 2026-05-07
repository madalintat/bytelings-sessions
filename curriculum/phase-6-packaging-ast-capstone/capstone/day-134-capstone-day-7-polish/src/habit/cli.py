"""CLI — polish pass.

Adds: -v/-vv, --quiet, ClickException-based errors, logging.
"""
from __future__ import annotations
import logging
from datetime import date, timedelta

import click

from . import storage
from .core import sort_key_streak

log = logging.getLogger("habit")


@click.group()
@click.version_option("0.1.0", package_name="habit")
@click.option("-v", "--verbose", count=True, help="-v for INFO, -vv for DEBUG.")
@click.option("-q", "--quiet", is_flag=True, help="Suppress success output.")
@click.pass_context
def main(ctx: click.Context, verbose: int, quiet: bool) -> None:
    """Track tiny daily habits."""
    level = (logging.WARNING, logging.INFO, logging.DEBUG)[min(verbose, 2)]
    logging.basicConfig(level=level, format="%(levelname)s %(message)s")
    ctx.ensure_object(dict)
    ctx.obj["quiet"] = quiet


def _say(ctx: click.Context, msg: str) -> None:
    if not ctx.obj.get("quiet"):
        click.echo(msg)


@main.command(name="list")
@click.option("--sort", type=click.Choice(["name", "streak"]), default="name",
              help="Sort order.")
@click.pass_context
def list_cmd(ctx: click.Context, sort: str) -> None:
    """List all habits with their current streak counts."""
    path = storage.default_data_path()
    log.debug("loading from %s", path)
    habits = storage.load(path)
    if not habits:
        _say(ctx, "(no habits yet — try `habit done <name>`)")
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
@click.pass_context
def done(ctx: click.Context, name: str) -> None:
    """Record that you completed <name> today.

    Auto-creates the habit if it doesn't exist yet.
    """
    if not name.strip():
        raise click.ClickException("habit name must not be empty")
    path = storage.default_data_path()
    habits = storage.load(path)
    today = date.today()
    habit = storage.mark_done(habits, name, today)
    storage.save(path, habits)
    log.info("recorded %s on %s", name, today)
    _say(ctx, f"recorded {name} on {today.isoformat()} ({habit.streak(today)}-day streak)")


@main.command()
@click.argument("name")
@click.option("--yes", is_flag=True, help="Skip confirmation prompt.")
@click.pass_context
def reset(ctx: click.Context, name: str, yes: bool) -> None:
    """Wipe history for <name>. Prompts unless --yes is given."""
    path = storage.default_data_path()
    habits = storage.load(path)
    if name not in habits:
        # ClickException prints "Error: no habit named 'foo'" and exits 1.
        raise click.ClickException(f"no habit named {name!r}")
    if not yes and not click.confirm(f"Really wipe history for {name!r}?"):
        _say(ctx, "aborted")
        return
    habits[name].clear()
    storage.save(path, habits)
    _say(ctx, f"reset {name}")


@main.command()
@click.option("--days", default=14, show_default=True,
              help="How many days of history to show.")
@click.pass_context
def recent(ctx: click.Context, days: int) -> None:
    """Show the last N days as a tiny grid (default 14)."""
    path = storage.default_data_path()
    habits = storage.load(path)
    if not habits:
        _say(ctx, "(no habits yet)")
        return
    today = date.today()
    window = [today - timedelta(days=days - 1 - i) for i in range(days)]
    width = max(len(name) for name in habits) + 2
    for name in sorted(habits):
        cells = " ".join("X" if d in habits[name].log else "." for d in window)
        click.echo(f"{name.ljust(width)}{cells}")
    legend = " ".join(d.strftime("%a")[0] for d in window)
    click.echo(f"{' ' * width}{legend}")
