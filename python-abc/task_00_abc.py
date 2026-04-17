#!/usr/bin/env python3
"""Module that defines an abstract class Animal and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method for animal sound."""
        pass


class Dog(Animal):
    """Subclass Dog that inherits from Animal."""

    def sound(self):
        """Returns the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass Cat that inherits from Animal."""

    def sound(self):
        """Returns the sound of a cat."""
        return "Meow"
