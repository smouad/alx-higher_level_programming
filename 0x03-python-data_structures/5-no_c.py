#!/usr/bin/python3
def no_c(my_string):
    res_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            res_string += i
    return res_string
