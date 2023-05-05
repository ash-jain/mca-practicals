"""
* Student Name - Aakash Jain.
* Roll No. - 222010019.
* Subject - Java and Python Lab.
* Lab Experiment 4 - Design a program to implement classes, inheritance, overloading and overriding.
"""

import math


class Shape:
    def __init__(self):
        pass

    def calculate_perimeter(self):
        raise NotImplementedError(
            "Subclass should override the abstract method.")

    def calculate_area(self):
        raise NotImplementedError(
            "Subclass should override the abstract method.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def calculate_perimeter(self):
        return 4 * self.length

    def calculate_area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth=None):
        if breadth is None:
            breadth = length

        self.length = length
        self.breadth = breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

    def calculate_area(self):
        return self.length * self.breadth


c = Circle(3)
print('Perimeter of the Circle: {0:.2f}.'.format(c.calculate_perimeter()))
print('Area of the Circle: {0:.2f}.\n'.format(c.calculate_area()))

s = Square(5)
print('Perimeter of the Square: {0:.2f}.'.format(s.calculate_perimeter()))
print('Area of the Square: {0:.2f}.\n'.format(s.calculate_area()))

r = Rectangle(4, 5)
print('Perimeter of the Rectangle: {0:.2f}.'.format(r.calculate_perimeter()))
print('Area of the Rectangle: {0:.2f}.'.format(r.calculate_area()))
