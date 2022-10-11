#!/usr/bin/python3

"""define class Square"""

class Square:
    """initiating square and attributes"""
    def __init__(self, size=0):
        """
        Args: (size=0) attributes an integer value to size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    def area(self):
        """initializing area of square"""
        return (self.__size * self.__size)
