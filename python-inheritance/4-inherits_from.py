#!/usr/bin/python3
"""""That modul chech inheritence or not"""


def inherits_from(obj, a_class):
    """used isinstance and is not"""
    return isinstance(obj, a_class) and type(obj) is not a_class
