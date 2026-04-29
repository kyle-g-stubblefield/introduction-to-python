"""
ashenmoor.world.zone
────────────────────
Zone class — the container for a self-contained area of the world.

A Zone owns:
  object_templates   dict[str, dict]   prototype dicts keyed by a short id
  mob_templates      dict[str, dict]   prototype dicts keyed by a short id
  rooms              dict[int, Room]   fully built rooms (objects+mobs already
                                       instantiated inside them)

Template dicts use the same keys as the Object / Item / Weapon / Mob
constructors, plus one extra key:

  "class"   the class to instantiate — Object, Item, Weapon, or Mob
            defaults to Object for object templates, Mob for mob templates

Usage inside a zone's rooms.py
───────────────────────────────
    from . import objects as O, mobs as M

    ROOMS = {
        1: Room({
            ...
            "objects": [O.spawn("red_marker"), O.spawn("sword")],
            "mobs":    [M.spawn("guard"), M.spawn("guard")],   # two guards
        })
    }

Two calls to spawn("guard") create two independent Mob instances — mutations
to one (hp loss, loot) do not affect the other.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .room import Room


class Zone:
    """
    A self-contained area: templates + pre-built rooms.

    Parameters
    ----------
    name             str
    rooms            dict[int, Room]
    object_templates dict[str, dict]   optional, default {}
    mob_templates    dict[str, dict]   optional, default {}
    """

    def __init__(
        self,
        name:             str,
        rooms:            dict,
        object_templates: dict | None = None,
        mob_templates:    dict | None = None,
    ):
        self.name             = name
        self.rooms            = rooms
        self.object_templates = object_templates or {}
        self.mob_templates    = mob_templates    or {}

    # ── Spawn helpers ─────────────────────────────────────────────────────────

    def spawn_object(self, key: str):
        """
        Create a fresh Object / Item / Weapon instance from a template.

        Raises KeyError if *key* is not in object_templates.
        """
        return _spawn(key, self.object_templates, _default_object_class)

    def spawn_mob(self, key: str):
        """
        Create a fresh Mob instance from a template.

        Raises KeyError if *key* is not in mob_templates.
        """
        return _spawn(key, self.mob_templates, _default_mob_class)

    def __repr__(self) -> str:
        return (f"Zone({self.name!r}, "
                f"{len(self.rooms)} rooms, "
                f"{len(self.object_templates)} obj templates, "
                f"{len(self.mob_templates)} mob templates)")


# ── Internal spawn machinery ──────────────────────────────────────────────────

def _default_object_class():
    from .objects import Object
    return Object

def _default_mob_class():
    from .mob import Mob
    return Mob

def _spawn(key: str, templates: dict, default_class_fn):
    """
    Look up *key* in *templates*, pick the class (or fall back to default),
    and return a new instance built from the remaining dict keys.

    Uses "spawn_as" (not "class") as the Python-class selector so it never
    collides with the character/mob "class" field (Warrior, Shaman, etc.).
    """
    if key not in templates:
        raise KeyError(f"No template named {key!r} in zone templates. "
                       f"Available: {list(templates)}")
    template = dict(templates[key])          # shallow copy — don't mutate original
    cls      = template.pop("spawn_as", None) or default_class_fn()
    return cls(template)


# ── Convenience: module-level spawn functions ─────────────────────────────────
# Each zone's objects.py and mobs.py exposes a module-level spawn() so rooms.py
# can call  O.spawn("key")  without needing a Zone instance at import time.

def make_spawner(templates: dict, default_class_fn):
    """
    Return a spawn(key) function bound to *templates*.

    Use this at the bottom of a zone's objects.py and mobs.py:

        from ashenmoor.world.zone import make_spawner
        spawn = make_spawner(TEMPLATES, lambda: Object)
    """
    def spawn(key: str):
        return _spawn(key, templates, default_class_fn)
    return spawn
