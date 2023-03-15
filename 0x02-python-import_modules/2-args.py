#!/usr/bin/env python3

import sys

args = sys.argv[1:] # exclude script name
num_args = len(args)

if num_args == 0:
    print("0 arguments.")
else:
    if num_args == 1:
        arg_str = "argument:"
    else:
        arg_str = "arguments:"
    print("{} {}{}".format(num_args, arg_str, "" if num_args == 0 else ":"))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
