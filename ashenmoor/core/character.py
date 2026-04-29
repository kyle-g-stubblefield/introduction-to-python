"""
ashenmoor.core.character
────────────────────────
Base Character class.

Characters hold raw base stats as a list[int] indexed by Stats enum order:
  [STR, DEX, CON, INT, WIS, CHA]

computed_stat() applies the character's racial multiplier on top.  The races
registry is passed in at construction time (or looked up from core.race.RACES
by default) so the class has no global-state dependency.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

from .stats import Stats

if TYPE_CHECKING:
    from .race import Race


class Character:
    """
    Base character (player or NPC).

    Parameters
    ----------
    d : dict
        'name'     str          character name
        'stats'    list[int]    [STR, DEX, CON, INT, WIS, CHA], default 80 each
        'race'     str          key into the races registry, default 'Human'
        'level'    int          default 1
        'position' str          default 'standing'
        'class'    str          class name, default 'Warrior'

    races : dict[str, Race] | None
        Race registry to use for computed_stat().
        Defaults to ashenmoor.core.race.RACES if not supplied.
    """

    def __init__(self, d: dict, races: dict | None = None):
        self.name:     str       = d.get("name",     "Unknown")
        self.stats:    list[int] = d.get("stats",    [80, 80, 80, 80, 80, 80])
        self.race:     str       = d.get("race",     "Human")
        self.level:    int       = d.get("level",    1)
        self.position: str       = d.get("position", "standing")
        self.cclass:   str       = d.get("class",    "Warrior")

        # Lazy-import to avoid circular deps; caller may supply their own registry
        if races is None:
            from .race import RACES
            races = RACES
        self._races = races

    # ── Stat access ───────────────────────────────────────────────────────────

    def get_stat(self, stat) -> int:
        """
        Raw base stat value.

        stat: int | str | Stats
        """
        if isinstance(stat, int):
            return self.stats[stat]
        if isinstance(stat, Stats):
            return self.stats[stat.value]
        if isinstance(stat, str):
            for s in Stats:
                if stat.lower() == s.abv:
                    return self.stats[s.value]
        raise ValueError(f"Unknown stat: {stat!r}")

    def computed_stat(self, stat) -> int:
        """Base stat × racial multiplier, truncated to int."""
        race = self._races.get(self.race)
        if race is None:
            return self.get_stat(stat)
        return int(self.get_stat(stat) * race.get_mod(stat))

    # ── Display ───────────────────────────────────────────────────────────────

    def character_sheet(self) -> str:
        """Return a formatted character sheet string (Diku color codes included)."""
        lines = [
            f"&+WCharacter sheet for &N{self.name}\n",
            f"&wRace:&N  {self.race}",
            f"&wClass:&N {self.cclass}",
            f"&wLevel:&N {self.level}",
            "&wStats:&N",
            (f"  &wStrength:&N     {self.get_stat('str'):>3}    "
             f"&wIntelligence:&N {self.get_stat('int'):>3}"),
            (f"  &wDexterity:&N    {self.get_stat('dex'):>3}    "
             f"&wWisdom:&N       {self.get_stat('wis'):>3}"),
            (f"  &wConstitution:&N {self.get_stat('con'):>3}    "
             f"&wCharisma:&N     {self.get_stat('cha'):>3}"),
        ]
        return "\n".join(lines)

    def pcs(self) -> None:
        """Print the character sheet via cprint (color-aware)."""
        from ..color import cprint
        cprint(self.character_sheet())

    def __str__(self) -> str:
        return self.character_sheet()

    def __repr__(self) -> str:
        return (f"Character(name={self.name!r}, race={self.race!r}, "
                f"class={self.cclass!r}, level={self.level})")
