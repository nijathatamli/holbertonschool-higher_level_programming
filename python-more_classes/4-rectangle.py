#!/usr/bin/python3


"""Module containing Rectangle class"""


class Rectangle:
    """This class represents a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    def area(self):
        """Function for calculating area"""
        return self.__height * self.__width
    def perimeter(self):
        """Function for calculating perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''
        return '\n'.join([self.__width * '#' for _ in range(self.__height)])

    def __repr__(self):
        """Method to return recreateable instance"""

        return f'Rectangle({self.__width}, {self.__height})'
