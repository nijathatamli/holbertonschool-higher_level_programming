#!/usr/bin/python3
"""Modul containing integer validator and area fucntions"""


class BaseGeometry:
    """Class for BaseGeometry"""
    def area(self):
        """Method to raise exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Method to validate integer"""
        if type(value) is not int:
            raise TypeError(name + " must be integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
