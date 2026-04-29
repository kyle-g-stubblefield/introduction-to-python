"""
ashenmoor.engine
────────────────
Game engine: state management, movement, command handling.

    from ashenmoor.engine import GameState, go, DIRECTIONS
"""

from .game import GameState, go, DIRECTIONS

__all__ = ["GameState", "go", "DIRECTIONS"]
