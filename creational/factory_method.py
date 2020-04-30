# when you want to increasre flexibility while creating new objects
import math
from abc import ABC, abstractmethod


class ShapeCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def count_figure_areas(self):
        shape = self.factory_method()
        rounded_shape_area = round(shape.count_area(), 2)

        result = f"Hey, I've just counted area of {shape}. It is {rounded_shape_area}cm squared!"
        return result


class Shape(ABC):

    @abstractmethod
    def count_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def count_area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle with radius {self.radius}cm"


class Triangle(Shape):
    def __init__(self, side, height=1):
        self.side = side
        self.height = height

    def count_area(self):
        return (self.side * self.height) / 2

    def __str__(self):
        return f"Triangle with side {self.side}cm and height {self.height}cm"


class CircleCreator(ShapeCreator):
    def __init__(self, radius):
        self.radius = radius

    def factory_method(self):
        return Circle(self.radius)


class TriangleCreator(ShapeCreator):
    def __init__(self, side, height=1):
        self.side = side
        self.height = height

    def factory_method(self):
        return Triangle(self.side, self.height)


creator = CircleCreator(20)
# creator = TriangleCreator(20)  # Uncomment to see the marvel!
print(creator.count_figure_areas())

