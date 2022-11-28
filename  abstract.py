from abc import ABC, abstractmethod
import math

class ShapeAbstract(ABC):
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    def get_color(self):
        return self.color

class Circle1(ShapeAbstract):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius**2

class Rectangle1(ShapeAbstract):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.height*self.width
