#!/usr/bin/env python3

import sys

try:
    if len(sys.argv) != 3:
        print("none")
    else:
        new_list = []
        for number in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
            new_list.append(number)
        print(new_list)
except:
    print("Invalid input")
