"""
zones
─────
Zone packages for Ashenmoor.

Each sub-package is a self-contained area.  Import the zone and call
GameState.load_zone() to bring it into the world:

    from zones.the_void import ZONE
    state.load_zone(ZONE)

Zone vnum ranges (room numbers must not overlap):
    the_void     1 – 99
"""
