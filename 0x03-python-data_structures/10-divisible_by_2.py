#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = ()
    for i in my_list:
        if i % 2 == 0:
            ret += (True,)
        else:
            ret += (False,)
    return ret
