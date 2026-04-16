#!/usr/bin/env python3
"""Module for Shape, Circle, Rectangle and Duck Typing."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class Shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print area and perimeter of a shape using duck typing."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
