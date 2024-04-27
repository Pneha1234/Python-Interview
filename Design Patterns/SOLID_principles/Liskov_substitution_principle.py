# Loskiv Substitution Principle(LSP): Subtypes must be substitutable for their base types.

# expmple
# shapes_lsp.py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

# Because a square is a special case of a rectangle with equal sides, you think of deriving a Square class from
# Rectangle in order to reuse the code. Then, you override the setter method for the .width and .height attributes so
# that when one side changes, the other side also changes:

# shapes_lsp.py

# ...

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["height"] = value

#  Unfortunately, this violates the Liskov substitution principle because you can’t replace instances of Rectangle with
#  their Square counterparts.
#
# When someone expects a rectangle object in their code, they might assume that it’ll behave like one by exposing two
# independent .width and .height attributes. Meanwhile, your Square class breaks that assumption by changing the
# behavior promised by the object’s interface.

# shapes_lsp.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side ** 2

# With this implementation in place, you can use the Shape type interchangeably with its Square and Rectangle subtypes
# when you only care about their common behavior:



def get_total_area(shapes):
    return sum(shape.calculate_area() for shape in shapes)

get_total_area([Rectangle(10, 5), Square(5)])

