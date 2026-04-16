#!/usr/bin/env python3
"""
Module for Fish, Bird and FlyingFish classes demonstrating multiple inheritance.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Standard swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Standard fish habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Standard flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Standard bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish, inheriting from Fish and Bird."""

    def fly(self):
        """Override fly method for flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method for flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method for flying fish."""
        print("The flying fish lives both in water and the sky!")
