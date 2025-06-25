#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    arg = sys.argv[1]
    para = input("What was the parameter? ")
    if arg == para:
        print("Good job!")
    else:
        print("Nope, sorry...")
