#!/usr/bin/python3
def best_score(my_dict):
    if not my_dict:
        return None
    max_value = max(my_dict.values())
    for key, value in my_dict.items():
        if value == max_value:
            return key

