#!/usr/bin/env python3

num = input()
try:
    num = int(num)
    if num < 0:
        print("This number is negative.")
    elif num > 0:
        print("This number is positive.")
    elif num == 0:
        print("This number is both positive and negative.")
except:
    print("Invalid input.")
