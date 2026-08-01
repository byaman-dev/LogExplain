"""
Knowledge base loader.

This module is responsible for locating and loading Markdown
knowledge base entries from disk.
"""

from pathlib import Path


def load_markdown(path: str | Path) -> str:
    """
    Load a Markdown knowledge base entry from disk.

    Args:
        path:
            Path to the Markdown file.

    Returns:
        The complete Markdown document as a string.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        IsADirectoryError:
            If the supplied path is a directory.

        UnicodeDecodeError:
            If the file cannot be decoded as UTF-8.
    """

    path = Path(path)

    return path.read_text(encoding="utf-8")
