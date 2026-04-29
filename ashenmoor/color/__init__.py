"""
ashenmoor.color
───────────────
Diku/ROM/SMAUG color-code renderer.

Imports everything you need directly from this subpackage:

    from ashenmoor.color import cprint, cinput, crepl, color, cstrip
    from ashenmoor.color import diku_to_ansi, diku_to_html
"""

from .diku_color import (
    # core converters
    diku_to_ansi,
    diku_to_html,
    # helpers
    color,
    cprint,
    cstrip,
    # interactive
    cinput,
    crepl,
    # internals exposed for advanced use
    ColorString,
    RESET,
)

__all__ = [
    "diku_to_ansi",
    "diku_to_html",
    "color",
    "cprint",
    "cstrip",
    "cinput",
    "crepl",
    "ColorString",
    "RESET",
]
