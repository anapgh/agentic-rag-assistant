"""Load saved prompts as .md files with this module."""

from functools import lru_cache
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent


@lru_cache
def load_prompt(name: str) -> str:
    """Return rompts/<name>.md content."""
    return (PROMPTS_DIR / f"{name}.md").read_text(encoding="utf-8")
