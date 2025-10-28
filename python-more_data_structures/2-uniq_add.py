#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for x in my_list:
        if type(x) == int:
            sum += x
    return sum
