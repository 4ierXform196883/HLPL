import math
from abc import ABC, abstractmethod


class Shape(ABC):
    name = "Shape"

    @abstractmethod
    def square(self):
        pass

    def __str__(self):
        return f"{self.name}: площадь = {self.square():.2f}"


class Rectangle(Shape):
    name = "Rectangle"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class Triangle(Shape):
    name = "Triangle"

    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Circle(Shape):
    name = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


if __name__ == "__main__":
    shapes = [Rectangle(3, 4), Triangle(3, 4, 5), Circle(1)]
    for shape in shapes:
        print(shape)
