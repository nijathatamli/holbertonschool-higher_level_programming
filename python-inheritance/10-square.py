#!/usr/bin/python3
"""class contains 2 functions"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """area() fucntions eixsts area of square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
