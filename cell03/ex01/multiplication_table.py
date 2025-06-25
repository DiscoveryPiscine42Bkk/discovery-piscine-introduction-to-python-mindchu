#!/usr/bin/env python3

num = input("Enter a number\n")
try:
    num = int(num)
    i = 0
    while i <= 9:
        print(f"{i} x {num} = {i * num}")
        i += 1
except:
    print("Invalid input.")
