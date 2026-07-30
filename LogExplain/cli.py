"""
Command-line interface for LogExplain.
"""

import typer

app = typer.Typer(
    name="logexplain",
    help="Understand security logs in plain English.",
)


if __name__ == "__main__":
    app()
