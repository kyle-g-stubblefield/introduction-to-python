"""
ashenmoor.core.stats
────────────────────
The six core attributes as an Enum.

Each member carries a short three-letter abbreviation via the .abv property,
which is used to look up stats by string ("str", "dex", etc.).
"""

from enum import Enum


class Stats(Enum):
    STRENGTH     = 0
    DEXTERITY    = 1
    CONSTITUTION = 2
    INTELLIGENCE = 3
    WISDOM       = 4
    CHARISMA     = 5

    @property
    def abv(self) -> str:
        """Three-letter lowercase abbreviation: 'str', 'dex', 'con' ..."""
        return self.name.lower()[:3]

    def __repr__(self) -> str:
        return f"Stats.{self.name}"
