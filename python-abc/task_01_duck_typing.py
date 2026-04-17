 HEAD
#!/usr/bin/python3
"""Module containing Shape class and its inheritances"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """The Shape class"""

    @abstractmethod
    def area(self):
        """Method for area"""
#!/usr/bin/env python3
"""
Module for Shape, Circle, Rectangle and Duck Typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Abstract method for area."""
 13ebb7155dfe9b885b1b3ceb708dcd8eb5a5ed76
        pass

    @abstractmethod
    def perimeter(self):
 HEAD
        """Method for perimeter"""
        """Abstract method for perimeter."""
 13ebb7155dfe9b885b1b3ceb708dcd8eb5a5ed76
        pass


class Circle(Shape):
HEAD
    """The Circle class inherited from Shape"""

    def __init__(self, radius):
        """Initialization wih radius"""
        self.radius = abs(radius)

    def area(self):
        """Returning duck area"""
        return pi * self.radius ** 2

    def perimeter(self):
        """Returning perimeter area"""
        return pi * self.radius * 2


class Rectangle(Shape):
    """The Rectangle class inherited from Shape"""

    def __init__(self, width, height):
        """Initialization wih width and height"""
=======
    """Circle class."""

    def __init__(self, radius):
        """Initialize Circle."""
        self.radius = radius

    def area(self):
        """Return area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize Rectangle."""
>>>>>>> 13ebb7155dfe9b885b1b3ceb708dcd8eb5a5ed76
        self.width = width
        self.height = height

    def area(self):
<<<<<<< HEAD
        """Returning duck area"""
        return self.width * self.height

    def perimeter(self):
        """Returning perimeter area"""
=======
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter."""
>>>>>>> 13ebb7155dfe9b885b1b3ceb708dcd8eb5a5ed76
        return 2 * (self.width + self.height)


def shape_info(obj):
<<<<<<< HEAD
    """Function to give shape info"""

    # Calculating the area and perimeter
    area = obj.area()
    perimeter = obj.perimeter()

    # Printing the area and perimeter
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
=======
    """Duck typing function."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
>>>>>>> 13ebb7155dfe9b885b1b3ceb708dcd8eb5a5ed76
