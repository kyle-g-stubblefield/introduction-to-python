"""
ashenmoor.world.objects
───────────────────────
Base world objects.

Hierarchy:
  Object          — any physical thing in the world (not takeable by default)
    Item          — a takeable Object with weight and stat mods
      Weapon      — an Item that can be wielded; has dice, hitroll, damroll

All classes are initialised from a dict `d` so zone-file loaders can pass
parsed data directly without needing to call constructors with keyword args.
"""


class Object:
    """
    A physical thing that can exist in a room.

    d keys
    ------
    name              str          short name shown in lists
    room_description  str          line shown in room description
    key_words         tuple[str]   words players can use to target this object
    description       str          full examine output
    """

    def __init__(self, d: dict):
        self.name:             str        = d.get("name",             "something")
        self.room_description: str        = d.get("room_description", "")
        self.key_words:        tuple[str] = d.get("key_words",        ())
        self.description:      str        = d.get("description",      "")
        self.take:             bool       = False   # Objects are not takeable

    def matches(self, keyword: str) -> bool:
        """True if keyword matches any of this object's key_words."""
        return keyword.lower() in (k.lower() for k in self.key_words)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Object({self.name!r})"


class Item(Object):
    """
    A takeable Object.  Adds weight and optional stat modifiers.

    d keys (in addition to Object)
    ------
    weight   int         weight in game units, default 0
    mod      list        stat modifier list (same index order as Stats enum)
    """

    def __init__(self, d: dict):
        super().__init__(d)
        self.weight: int  = d.get("weight", 0)
        self.mod:    list = d.get("mod",    [])
        self.take:   bool = True

    def __repr__(self) -> str:
        return f"Item({self.name!r}, weight={self.weight})"


class Weapon(Item):
    """
    A wieldable Item.

    d keys (in addition to Item)
    ------
    dice      str   damage dice string e.g. '2d6', default '1d6'
    hitroll   int   to-hit bonus,  default 0
    damroll   int   damage bonus,  default 0
    """

    def __init__(self, d: dict):
        super().__init__(d)
        self.dice:    str = d.get("dice",    "1d6")
        self.hitroll: int = d.get("hitroll", 0)
        self.damroll: int = d.get("damroll", 0)

    def __repr__(self) -> str:
        return f"Weapon({self.name!r}, dice={self.dice!r})"
