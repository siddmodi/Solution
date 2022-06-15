'''
Abstract class works like a base class
By using this we can set some we can say rules for another classes like here in this example
    if we don't define printarea function in Rectangle,Square,Circle classes the it throws an error
Using this abstarct class we can set some boundation for programmers if they wanna use parameters or any function of this 
    class then they have to define this or that function etc.
'''

import math

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

class Square(Shape):
    type = "Square"
    sides = 4
    def __init__(self,length):
        self.length = length
    def printarea(self):
        return self.length^2

class Circle(Shape):
    type = "Circle"
    sides = 0
    def __init__(self,radius):
        self.radius = radius
    def printarea(self):
        r2 = self.radius^2
        area = (math.pi)*r2
        return area



rect = Rectangle(5,6)
sq = Square(5)
cir = Circle(3)

print(rect.printarea())
print(sq.printarea())
print(cir.printarea())
