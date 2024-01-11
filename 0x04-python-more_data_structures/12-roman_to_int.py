#!/usr/bin/python3
def roman_to_int(roman_string):
    res = 0
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    for num in roman_string:
        res += my_dict[num]
    return res
