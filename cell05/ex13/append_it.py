#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    i = 1
    while i < len(sys.argv):
        word = sys.argv[i]
        if word[-3:] != "ism":
            print(f"{word}ism")
        i += 1
