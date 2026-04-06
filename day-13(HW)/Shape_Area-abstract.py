from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def area(self):         # child MUST implement this
        pass

    def describe(self):     # regular method — uses abstraction
        print(f'Area: {self.area():.2f}')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):         # must implement
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def area(self):         # must implement
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base   = base
        self.height = height

    def area(self):         # must implement
        return 0.5 * self.base * self.height


# Test — try creating object from abstract class first:
# s = Shape()              # should raise TypeError

shapes = [Circle(7), Rectangle(5, 10), Triangle(6, 8)]
for shape in shapes:
    shape.describe()