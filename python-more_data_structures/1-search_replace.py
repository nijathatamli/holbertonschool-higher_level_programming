#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for i, x in enumerate(my_list):
        if x == search:
            new[i] = replace
    return new
