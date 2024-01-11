#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    for key in a_dictionary:
        if a_dictionary[key] > score:
            score = a_dictionary[key]
    for key, value in a_dictionary.items():
        if value == score:
            return key
    return None
