# OCP(Open closed principle):- Software entities(classes, modules, functions, etc), should be open for extension, but
# closed for modification.

# example
# shapes_ocp.py

from math import pi

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2

# now lets say we want to add a new shape, maybe a square. How would we do that? the option here is to add another elif
# clause to __init__() and to calculate_area() so that we can address the requirements of a square shape.

# having to make these changes to create new shapes means that your class is open to modification. That violates the
# open-closed principle.

# the solution to this problem will be:
# shapes_ocp.py

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2

# This update closes the class to modifications. Now you can add new shapes to your class design without the need to
# modify Shape.