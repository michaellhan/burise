from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Compute area of the shape."""
        pass

class Square(Shape):
    def __init__(self, side: float):
        # store side length
        self.side = side

    def area(self):
        return self.side**2

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius**2