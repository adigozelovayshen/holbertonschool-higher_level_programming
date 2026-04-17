#!/usr/bin/python3
from task_01_duck_typing import Circle, Rectangle, shape_info

# Circle (radius = 5) testi
circle = Circle(radius=5)
# Rectangle (width = 4, height = 7) testi
rectangle = Rectangle(width=4, height=7)

print("--- Circle Info ---")
shape_info(circle)

print("\n--- Rectangle Info ---")
shape_info(rectangle)
