#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ret_list = []
    for elem in my_list:
        if elem == search:
            ret_list.append(replace)
        else:
            ret_list.append(elem)
    return ret_list
