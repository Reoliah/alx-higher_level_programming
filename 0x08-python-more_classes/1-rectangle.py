#!/usr/bin/python3
"""
Real definition of a Rectangle must include width and height
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        # initializing properties of a rectangle

        self.width = width
        self.height = height

    @property
    # defining the private instance attributes

    def width(self):
        print("retrieving the width")
        
        return self.__width

    def height(self):
        print("retrieving the height")

        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        size.__height = value
