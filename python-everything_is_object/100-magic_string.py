#!/usr/bin/python3
def magic_string():
    magic_string.count =  getattr(magic_string.count, "count", 0) + 1
    return ", ".join(magic_string.count * ["Best School"])
