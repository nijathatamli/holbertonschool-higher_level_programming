#!/usr/bin/python3
"""Module containing Rectangle class"""

class Rectangle:
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
        if not  isinstance(value):
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
        if not isinstance(value):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError('width must be greater than 0')
        self.__height = value
