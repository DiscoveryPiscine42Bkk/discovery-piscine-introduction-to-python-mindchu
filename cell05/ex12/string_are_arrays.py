#!/usr/bin/env python3

import sys

count = 0
i = 1
while i < len(sys.argv):
    j = 0
    while j < len(sys.argv[i]):
        str = sys.argv[i][j]
        if str == 'z':
            print("z", end="")
            count = 1
        j += 1
    i += 1
if count == 1:
    print()
else:
    print("none")
