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
        """Calculates the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initializes Circle."""
        self.__radius = radius

    def area(self):
        """Returns area."""
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """Returns perimeter."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initializes Rectangle."""
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter."""
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """Duck typing function to print shape info."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
