"""
ashenmoor.core
──────────────
Core character system: stats, races, characters.

    from ashenmoor.core import Stats, Race, RACES, Character
"""

from .stats     import Stats
from .race      import Race, RACES
from .character import Character

__all__ = ["Stats", "Race", "RACES", "Character"]
