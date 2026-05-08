"""Click-based CLI for the bytelings runner."""
from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path

import click

from . import locator
from . import progress as progress_mod
from . import ui

WELCOME_TEXT = """\
[bold]Welcome to bytelings.[/bold]

Small daily exercises that make you fluent at writing and reading code.
Inspired by [cyan]Rustlings[/cyan]; built for Python today, with C, C++,
Rust, and Go on the roadmap.

Each day is one concept taught in 5 rungs:
  1. Read a short concept page
  2. Fix a broken file (fluency drill)
  3. Fill a function body (guided)
  4. Implement from scratch (solo, hidden tests)
  5. Apply the concept in a tiny project chunk

Run [cyan]bytelings[/cyan] (no args) to start the watcher. Save your
file → tests run → green panel → next rung. That's the loop.

Other commands:
  [cyan]bytelings init[/cyan]      — create ./bytelings/ with curriculum + scaffold
  [cyan]bytelings today[/cyan]     — what you're working on now
  [cyan]bytelings progress[/cyan]  — streak + completion bar
  [cyan]bytelings hint[/cyan]      — show today's concept page
  [cyan]bytelings run[/cyan]       — run current rung's tests once
  [cyan]bytelings done[/cyan]      — manually mark current rung done
  [cyan]bytelings reset DAY[/cyan] — reset a day's progress
"""

PRE_INIT_HINT = """\
[bold yellow]No curriculum/ folder here.[/bold yellow]

Run [cyan]bytelings init[/cyan] to create a [cyan]./bytelings/[/cyan] project folder, then
[cyan]cd bytelings && uv sync && bytelings[/cyan] to start the watcher.
"""


def _curriculum_source() -> Path:
    """Locate the bundled curriculum inside the installed package.

    Falls back to the repo's `curriculum/` for editable / dev installs.
    """
    bundled = resources.files("bytelings") / "_curriculum"
    if bundled.is_dir():
        return Path(str(bundled))
    repo_curriculum = Path(__file__).resolve().parent.parent / "curriculum"
    if repo_curriculum.is_dir():
        return repo_curriculum
    raise click.ClickException(
        "Could not locate the bundled curriculum. Reinstall bytelings or "
        "run from the repo root."
    )


def _scaffold_source() -> Path | None:
    """Locate the bundled student scaffold (pyproject.toml + uv.lock).

    Returns None if no scaffold is bundled (older installs).
    Falls back to the repo's `scaffold/` for editable / dev installs.
    """
    bundled = resources.files("bytelings") / "_scaffold"
    if bundled.is_dir():
        return Path(str(bundled))
    repo_scaffold = Path(__file__).resolve().parent.parent / "scaffold"
    if repo_scaffold.is_dir():
        return repo_scaffold
    return None


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context) -> None:
    """bytelings — small daily exercises to make you fluent at code.

    Run with no subcommand to launch the watcher.
    """
    if ctx.invoked_subcommand is not None:
        return
    if not Path("curriculum").is_dir():
        ui.console.print(PRE_INIT_HINT)
        ctx.exit(1)
    from . import watcher  # lazy — keeps CLI tests off watchdog
    watcher.watch()


@cli.command()
@click.option(
    "--target", "-t", default="bytelings",
    help="Project directory to create (default: ./bytelings).",
    type=click.Path(file_okay=False, path_type=Path),
)
@click.option(
    "--force", is_flag=True,
    help="Overwrite an existing target directory.",
)
def init(target: Path, force: bool) -> None:
    """Create TARGET project directory (default ./bytelings) with the
    bundled curriculum and a uv-ready pyproject.toml inside.

    Then: cd TARGET && uv sync && bytelings
    """
    src = _curriculum_source()
    if target.exists():
        if not force:
            raise click.ClickException(
                f"{target} already exists. Re-run with --force to overwrite."
            )
        shutil.rmtree(target)
    shutil.copytree(src, target / "curriculum")

    scaffold_src = _scaffold_source()
    shipped: list[str] = []
    if scaffold_src is not None:
        for fname in ("pyproject.toml", "uv.lock"):
            f = scaffold_src / fname
            if not f.is_file():
                continue
            shutil.copy2(f, target / fname)
            shipped.append(fname)

    ui.console.print(f"[bold green]✔ Created ./{target}/[/bold green]")
    if shipped:
        ui.console.print(f"  shipped: {', '.join(shipped)}")
    ui.console.print(
        f"\n[dim]Next:[/dim] [cyan]cd {target} && uv sync && bytelings[/cyan]"
    )


@cli.command()
def welcome() -> None:
    """Print the one-time onboarding intro."""
    ui.console.print(WELCOME_TEXT)


@cli.command()
def today() -> None:
    """Show today's day and rung plan."""
    p = progress_mod.load()
    day = locator.current_or_next_day(p)
    if day is None:
        ui.header("All 135 days complete! 🎉")
        click.echo("Or — run `bytelings init` to scaffold the curriculum.")
        return
    ui.header(f"{day.slug}")
    rungs = locator.rungs_of(day)
    ui.rung_table(rungs, p.current_rung, p.completed_rungs_today)
    click.echo(
        f"\nPhase: {day.phase}    Module: {day.module}\n"
        f"Run `bytelings` to start the watcher."
    )


@cli.command(name="progress")
def progress_cmd() -> None:
    """Show streak and overall progress."""
    p = progress_mod.load()
    days = locator.all_days()
    total = len(days)
    completed = len(p.completed_days)
    ui.progress_summary(completed, total, p.streak_days, p.longest_streak)


@cli.command()
def watch() -> None:
    """Run the watcher (the main loop). Ctrl-C to stop."""
    from . import watcher
    watcher.watch()


@cli.command()
@click.argument("day_slug", required=False)
def run(day_slug: str | None) -> None:
    """Run the current rung's tests once (no watch).

    With DAY_SLUG, run that day's current rung instead of today's.
    """
    from . import watcher
    p = progress_mod.load()
    day = locator.find_day(day_slug) if day_slug else locator.current_or_next_day(p)
    if day is None:
        click.echo(f"Day not found: {day_slug}" if day_slug else "No day to run.")
        return
    rungs = locator.rungs_of(day)
    rung = locator.rung_for(p, rungs)
    if rung.test_file is None:
        click.echo(f"Rung {rung.number} has no automated tests.")
        return
    result = watcher.run_pytest(rung.test_file)
    if result.passed:
        ui.banner_pass(f"Rung {rung.number}: {rung.name}")
    else:
        ui.banner_fail(result.summary)


@cli.command()
@click.argument("day_slug", required=False)
def hint(day_slug: str | None) -> None:
    """Show the current (or named) day's concept page.

    The concept page is your hint — read it whenever you're stuck.
    """
    p = progress_mod.load()
    day = locator.find_day(day_slug) if day_slug else locator.current_or_next_day(p)
    if day is None:
        click.echo(f"Day not found: {day_slug}" if day_slug else "No day to hint.")
        return
    concept = day.path / "concept.md"
    if not concept.is_file():
        click.echo(f"No concept.md for {day.slug}.")
        return
    ui.header(f"Concept: {day.slug}")
    ui.console.print(concept.read_text())


@cli.command()
def done() -> None:
    """Manually mark the current rung complete (escape hatch)."""
    p = progress_mod.load()
    day = locator.current_or_next_day(p)
    if day is None:
        click.echo("No day in progress.")
        return
    p.current_day = day.slug
    rung = p.current_rung
    next_day = next(
        (d for d in locator.all_days()
         if d.slug not in p.completed_days and d.slug != day.slug),
        None,
    )
    p = progress_mod.advance_after_pass(
        p, day.slug, rung, next_day.slug if next_day else None
    )
    progress_mod.save(p)
    if rung == progress_mod.TOTAL_RUNGS:
        ui.banner_day_complete(day.slug, p.streak_days)
    else:
        ui.banner_pass(f"Rung {rung} marked done")


@cli.command(name="next")
def next_cmd() -> None:
    """Skip to next rung without finishing the current one."""
    p = progress_mod.load()
    if p.current_rung < progress_mod.TOTAL_RUNGS:
        p.current_rung += 1
        progress_mod.save(p)
        click.echo(f"Skipped to rung {p.current_rung}.")
    else:
        click.echo("Already on rung 5. Use `bytelings done` to finish the day.")


@cli.command()
@click.argument("day_slug")
def reset(day_slug: str) -> None:
    """Reset progress for a specific day."""
    p = progress_mod.load()
    if day_slug in p.completed_days:
        p.completed_days.remove(day_slug)
    if p.current_day == day_slug:
        p.current_rung = 1
        p.completed_rungs_today = []
    progress_mod.save(p)
    click.echo(f"Reset {day_slug}.")


@cli.command()
@click.argument("day_slug_or_number")
def start(day_slug_or_number: str) -> None:
    """Jump the watcher to a specific day. Pass the slug or the day number.

    Examples: `bytelings start day-007-string-methods-and-fstrings`
              `bytelings start 7`
    """
    days = locator.all_days()
    if not days:
        raise click.ClickException("No curriculum scaffolded. Run `bytelings init` first.")
    target = None
    if day_slug_or_number.isdigit():
        n = int(day_slug_or_number)
        target = next((d for d in days if d.number == n), None)
    else:
        target = next((d for d in days if d.slug == day_slug_or_number), None)
    if target is None:
        raise click.ClickException(f"No such day: {day_slug_or_number}")
    p = progress_mod.load()
    p.current_day = target.slug
    p.current_rung = 1
    p.completed_rungs_today = []
    progress_mod.save(p)
    click.echo(f"Now on {target.slug}. Run `bytelings` to start the watcher.")


@cli.command()
def list() -> None:
    """List every day in the curriculum with completion markers."""
    p = progress_mod.load()
    days = locator.all_days()
    if not days:
        click.echo("No curriculum scaffolded. Run `bytelings init` first.")
        return
    completed = set(p.completed_days)
    for d in days:
        marker = "[green]✔[/green]" if d.slug in completed else "[dim]○[/dim]"
        line = f"{marker} {d.slug}  [dim]({d.module})[/dim]"
        ui.console.print(line)


@cli.command(name="phase-project")
def phase_project() -> None:
    """Open the README for the current phase project (if at a boundary)."""
    p = progress_mod.load()
    day = locator.first_unfinished_day(p)
    if day is None:
        click.echo("All days complete.")
        return
    phase_dir = Path("curriculum") / day.phase
    candidates = list(phase_dir.glob("phase-*-project-*/README.md"))
    if candidates:
        click.echo(f"Phase project: {candidates[0]}")
    else:
        click.echo(f"No phase project found for {day.phase}.")


if __name__ == "__main__":
    cli()
