#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    i = 1
    while i < len(sys.argv):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
        i += 1
