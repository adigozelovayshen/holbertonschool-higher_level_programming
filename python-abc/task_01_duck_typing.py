#!/usr/bin/env python3
"""
Module defining Shape, Circle, Rectangle and shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        """
        Initialize the Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    Standalone function that prints the area and perimeter of a shape.
    Relies on duck typing.
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
