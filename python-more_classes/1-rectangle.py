#!/usr/bin/python3
"""Module containing Rectangle class"""

class Rectangle:
    """This class about rectangle"""
    
    def __init__(self,  width = 0, height = 0):
        self.width = width
        self.height = height
    @property
    def width(self):
        """Getter for __width"""
        return self.__width
    @width.setter
    def width(self, value):
        """Setter for __width"""
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError('width must be greater than 0')
        self.__width = value
    @property
    def height(self):
        """Getter for __width"""
        return self.__height
    @height.setter
    def height(self,value):
        """Setter for __width"""
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError('width must be greater than 0')
        self.__height = value
