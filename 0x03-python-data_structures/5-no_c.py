#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(i): None for i in 'cC'})
    # new_string = "".join([char for char in my_string if char not in 'cC'])
    return new_string
