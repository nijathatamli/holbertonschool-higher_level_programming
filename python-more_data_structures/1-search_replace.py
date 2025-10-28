#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i,x in enumerate(my_list):
        if x == search:
            my_list[i] = replace
    return my_list
