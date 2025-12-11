#!/usr/bin/python3

"function that returns the list of available attributes and methods of an object"

def lookup(obj):
    "we used dir fucntion which return list of attributes"
    return list(dir(obj))
