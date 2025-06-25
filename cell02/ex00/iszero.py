#!/usr/bin/env python3

num = input()
try:
    num = int(num)
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")
except:
    print("Invalid input.")
