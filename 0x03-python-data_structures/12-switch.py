#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b)) # tuple unpacking to swap the values of a and b in one line