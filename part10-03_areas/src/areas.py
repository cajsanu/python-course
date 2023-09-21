# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.width}x{self.height}"

    def area(self):
        return self.width * self.height
    
    
class Square(Rectangle):
    def __init__(self, width, height: int=None):
        super().__init__(width, height)
        
    def area(self):
        return self.width * self.width
    
    def __str__(self):
        return f"square {self.width}x{self.width}"
    
    
# square = Square(4)
# print(square)
# print("area:", square.area())
