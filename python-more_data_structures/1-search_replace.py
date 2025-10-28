#!/usr/bin/python3
def search_replace(my_list, search, replace):
    index_of_search = my_list.index(search)
    index_of_replace = my_list.index(replace)
    my_list[index_of_search], my_list[index_of_replace] = my_list[index_of_replace], my_list[index_of_search]
    return my_list
