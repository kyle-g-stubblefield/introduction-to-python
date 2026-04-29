"""
zones.the_void.objects
──────────────────────
Object templates for The Void zone.

Add an entry to TEMPLATES for every object that can appear in this zone.
The "class" key picks the instantiation class (Object / Item / Weapon).
Omitting "class" defaults to Object.

Call spawn(key) to get a fresh independent instance.
"""

from ashenmoor.world import Object, Item, Weapon
from ashenmoor.world.zone import make_spawner

TEMPLATES: dict[str, dict] = {

    "red_marker": {
        "spawn_as":         Object,
        "name":             "a &rred expo marker&N",
        "key_words":        ("red", "expo", "marker"),
        "room_description": "A &rred expo marker&N has been carelessly discarded here.",
        "description":      "A dark magenta low-scent dry-erase marker, about half used.",
    },

    "green_marker": {
        "spawn_as":         Object,
        "name":             "a &ggreen expo marker&N",
        "key_words":        ("green", "expo", "marker"),
        "room_description": "A &ggreen expo marker&N has been carelessly discarded here.",
        "description":      "A forest green low-scent dry-erase marker, about half used.",
    },

    "silken_sack": {
        "spawn_as":         Item,
        "name":             "a &+rtattered &+csilken sack&N",
        "key_words":        ("tattered", "silken", "sack"),
        "room_description": "A &+rtattered &+csilken sack&N lies here, discarded.",
        "description":      "This sack seems to be in an awful condition.",
        "weight":           2,
    },

    "elven_scimitar": {
        "spawn_as":         Weapon,
        "name":             "&+ga &wg&Wl&wi&Wtt&wer&Wi&wng &N&+gelven scimitar&N",
        "key_words":        ("glittering", "elven", "scimitar"),
        "room_description": (
            "&+gA glittering elven scimitar&N lies on the ground here."
        ),
        "description":      "&+gIts blade is encrusted with diamond dust.&N",
        "weight":           3,
        "dice":             "2d8",
        "hitroll":          2,
        "damroll":          4,
    },

}

# Module-level spawn — rooms.py calls  O.spawn("red_marker")
spawn = make_spawner(TEMPLATES, lambda: Object)
