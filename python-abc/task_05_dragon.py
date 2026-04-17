#!/usr/bin/env python3
"""
Module defining Mixins and a Dragon class.
"""


class SwimMixin:
    """Mixin to add swimming functionality."""

    def swim(self):
        """Prints swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to add flying functionality."""

    def fly(self):
        """Prints flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly and roar."""

    def roar(self):
        """Prints dragon's roar message."""
        print("The dragon roars!")
