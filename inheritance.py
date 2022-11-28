import math
class Shape():
    def __init__(self, border_color, border_thickness, location) -> None:
        self.border_color = border_color
        self.border_thickness = border_thickness
        self.location = location
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: ({self.border_color}, {self.border_thickness}, {self.location})"
    
    def change_border_color(self, color) -> None:
        self.border_color = color
    
    def change_border_thickness(self, thickness) -> None:
        self.border_thickness = thickness
    
    def change_location(self, location) -> None:
        self.location = location


class Circle(Shape):
    def __init__(self, border_color, border_thickness, location, radius) -> None:
        super().__init__(border_color, border_thickness, location)
        self.radius = radius
    
    def __str__(self) -> str:
       return f"{super().__str__()}, {self.radius}"
    
    def area(self):
        return math.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self, border_color, border_thickness, location, length, breadth) -> None:
        super().__init__(border_color, border_thickness, location)
        self.length = length
        self.breadth = breadth
    
    def __str__(self) -> str:
        return f"{super().__str__()}, length: {self.length}, breadth: {self.breadth}"
    
    def area(self):
        return self.length*self.breadth

class Square(Shape):
    def __init__(self, border_color, border_thickness, location, length) -> None:
        super().__init__(border_color, border_thickness, location)
        self.length = length
    
    def __str__(self) -> str:
        return f"{super().__str__()}, length: {self.length}"