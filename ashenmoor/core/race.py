"""
ashenmoor.core.race
───────────────────
Race base class and the default race registry.

A Race holds:
  stats_modifiers  list[float]  multiplier per stat (index matches Stats enum)
  innate_abilities list[str]    strings like 'infravision', 'doorbash'
  size             str          'small', 'medium_small', 'medium', 'large', etc.

Stat lookup follows the Stats enum order:
  [STR, DEX, CON, INT, WIS, CHA]
   [0]  [1]  [2]  [3]  [4]  [5]
"""

from .stats import Stats


class Race:
    """
    Base race. Stores per-stat multipliers and innate abilities.

    Parameters
    ----------
    d : dict
        'stats_modifier'   list of 6 floats, default [1,1,1,1,1,1]
        'innate_abilities' list of str,       default []
        'size'             str,               default 'medium'
    """

    def __init__(self, d: dict | None = None):
        if d is None:
            d = {}
        self.stats_modifiers:  list[float] = d.get("stats_modifier",   [1, 1, 1, 1, 1, 1])
        self.innate_abilities: list[str]   = d.get("innate_abilities",  [])
        self.size:             str         = d.get("size",              "medium")

    def get_mod(self, stat) -> float:
        """
        Return the multiplier for *stat*.

        stat can be:
          int        → index directly (0=STR … 5=CHA)
          str        → three-letter abbrev ('str', 'dex', 'con', 'int', 'wis', 'cha')
          Stats      → enum member
        """
        if isinstance(stat, int):
            return self.stats_modifiers[stat]
        if isinstance(stat, Stats):
            return self.stats_modifiers[stat.value]
        if isinstance(stat, str):
            for s in Stats:
                if stat.lower() == s.abv:
                    return self.stats_modifiers[s.value]
        raise ValueError(f"Unknown stat: {stat!r}")

    def __repr__(self) -> str:
        return f"Race(size={self.size!r}, abilities={self.innate_abilities})"


# ── Default race registry ─────────────────────────────────────────────────────
# Keys are the canonical race name strings used in Character dicts.

RACES: dict[str, Race] = {
    "Human": Race(),

    "Dwarf": Race({
        "stats_modifier":   [1.1, 1.0, 1.3, 0.9, 1.0, 1.0],
        "size":             "medium_small",
        "innate_abilities": ["infravision"],
    }),

    "Grey Elf": Race({
        "stats_modifier":   [0.7, 1.2, 0.8, 1.1, 1.0, 1.1],
        "size":             "medium_small",
        "innate_abilities": ["infravision", "outdoor_sneak"],
    }),

    "Ogre": Race({
        "stats_modifier":   [1.5, 0.8, 1.5, 0.5, 0.75, 0.75],
        "size":             "large",
        "innate_abilities": ["doorbash"],
    }),
}
