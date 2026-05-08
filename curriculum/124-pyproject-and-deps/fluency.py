"""Rung 2: Fluency drill — parse a pyproject.toml fragment.

Topic: tomllib basics + reading [project] metadata

Two TODOs. Use tomllib (stdlib, 3.11+). The tests parse a small string
of TOML and check you pull the right keys out.
"""
import tomllib


def parse_project_name(toml_text: str) -> str:
    """Return the value of [project].name from a TOML string."""
    # TODO: tomllib.loads expects... what type of argument?
    data = tomllib.loads(toml_text.encode())
    return data["project"]["name"]


def list_dependencies(toml_text: str) -> list[str]:
    """Return the [project].dependencies list, or [] if missing."""
    data = tomllib.loads(toml_text)
    # TODO: this raises KeyError when dependencies is absent.
    return data["project"]["dependencies"]
