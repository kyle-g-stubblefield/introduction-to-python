"""
ashenmoor.world.room
────────────────────
Room class and terrain constants.

A Room holds:
  number       int          unique room ID (used as dict key in world state)
  name         str          short title shown on entry
  description  str          long description (may contain Diku color codes)
  indoors      bool         affects weather / lighting
  terrain      str          one of TERRAIN
  exits        list[dict]   each: {'direction': str, 'roomId': int}
  objects      list         Object instances currently in the room

Characters are NOT stored on the Room — they live in a GameState.locations
dict (character_name -> room_number) so that rooms themselves remain
stateless and serialisable.  Room.get_characters() accepts the locations
and characters dicts as arguments instead of reading globals.
"""


TERRAIN = ("no ground", "water", "mountain", "plain", "stone", "forest",
           "desert", "swamp", "road", "inside")


class Room:
    """
    A single location in the world.

    Parameters
    ----------
    d : dict
        'number'       int
        'name'         str
        'description'  str
        'indoors'      bool
        'terrain'      str   (should be one of TERRAIN)
        'exits'        list[dict]   e.g. [{'direction':'north','roomId':2}, ...]
        'objects'      list         Object instances
    """

    def __init__(self, d: dict):
        self.number:      int        = d["number"]
        self.name:        str        = d["name"]
        self.description: str        = d["description"]
        self.indoors:     bool       = d.get("indoors", False)
        self.terrain:     str        = d.get("terrain", "plain")
        self.exits:       list[dict] = d.get("exits",   [])
        self.objects:     list       = d.get("objects", [])
        self.mobs:        list       = d.get("mobs",    [])

    # ── Exit helpers ──────────────────────────────────────────────────────────

    def exit_room_id(self, direction: str) -> int | None:
        """Return the roomId for *direction*, or None if no exit that way."""
        for ex in self.exits:
            if ex["direction"].lower() == direction.lower():
                return ex["roomId"]
        return None

    def _exits_str(self) -> str:
        if not self.exits:
            return "&gExits:&N &RNone!&N"
        parts = ["&gExits:&N"]
        for i, ex in enumerate(self.exits):
            sep = " &C-&N" if i > 0 else ""
            parts.append(f"{sep} &c{ex['direction'].title()}&N")
        return "".join(parts)

    # ── Object helpers ────────────────────────────────────────────────────────

    def _objects_str(self) -> str:
        if not self.objects:
            return ""
        return "\n".join(obj.room_description for obj in self.objects)

    def _mobs_str(self) -> str:
        if not self.mobs:
            return ""
        return "\n".join(
            mob.room_description if mob.room_description
            else f"{mob.name.capitalize()} is here."
            for mob in self.mobs
        )

    # ── Character helpers (stateless — caller supplies current locations) ──────

    def get_characters(self, locations: dict, characters: dict) -> list:
        """Return list of Character objects currently in this room."""
        return [characters[name]
                for name, room_id in locations.items()
                if room_id == self.number and name in characters]

    def _characters_str(self, locations: dict, characters: dict) -> str:
        chars = self.get_characters(locations, characters)
        if not chars:
            return ""
        return "\n".join(f"{c.name.title()} stands here" for c in chars)

    # ── Display ───────────────────────────────────────────────────────────────

    def render(self, locations: dict | None = None,
               characters: dict | None = None) -> str:
        """
        Return the full room string (Diku color codes included).

        locations  / characters are optional; pass them to show who's present.
        """
        parts = [f"&+W{self.name}&N", f"  {self.description}"]
        parts.append(self._exits_str())
        mob_str = self._mobs_str()
        if mob_str:
            parts.append(mob_str)
        obj_str = self._objects_str()
        if obj_str:
            parts.append(obj_str)
        if locations is not None and characters is not None:
            char_str = self._characters_str(locations, characters)
            if char_str:
                parts.append(char_str)
        return "\n".join(parts)

    def __repr__(self) -> str:
        """
        Default repr delegates to render() with no character tracking.
        Game engine passes locations+characters explicitly via render().
        """
        return self.render()

    def __str__(self) -> str:
        return self.render()
