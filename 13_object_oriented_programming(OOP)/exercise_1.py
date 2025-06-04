#Write a class Rectangle that has width and height attributes and a method area that returns the area of the rectangle.
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

r = Rectangle(4,7)
print(r.area())
