#!/usr/bin/python3
"""Square class contains 3 functions, both of them are dunder methods"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """area print area of square, others are dunder"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
