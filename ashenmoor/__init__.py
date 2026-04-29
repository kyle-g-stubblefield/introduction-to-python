"""
ashenmoor
─────────
A Python MUD framework.

Subpackages
───────────
  ashenmoor.color    Diku/ROM/SMAUG color codes → ANSI / HTML
  ashenmoor.core     Stats enum, Race, Character
  ashenmoor.world    Object, Item, Weapon, Room
  ashenmoor.engine   GameState, movement, command loop

Quick start
───────────
    from ashenmoor.color  import cprint, cinput, crepl
    from ashenmoor.core   import Stats, Race, RACES, Character
    from ashenmoor.world  import Object, Item, Weapon, Room
    from ashenmoor.engine import GameState

    state = GameState()
    state.load_world(rooms, characters, locations, player="Moted")

    crepl(
        handler  = state.handle,
        prompt   = "&g>&N ",
        banner   = "&+WWelcome to Ashenmoor&N",
        farewell = "&CGoodbye!&N",
    )
"""

# Flat convenience imports — `from ashenmoor import cprint` just works
from .color  import cprint, cinput, crepl, color, cstrip
from .core   import Stats, Race, RACES, Character
from .world  import Object, Item, Weapon, Room, TERRAIN
from .engine import GameState, go

__all__ = [
    # color
    "cprint", "cinput", "crepl", "color", "cstrip",
    # core
    "Stats", "Race", "RACES", "Character",
    # world
    "Object", "Item", "Weapon", "Room", "TERRAIN",
    # engine
    "GameState", "go",
]
