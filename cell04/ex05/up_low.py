#!/usr/bin/env python3

inp = input()
for char in inp:
    if char.isupper():
        print(char.lower(), end="")
    elif char.islower():
        print(char.upper(), end="")
    else:
        print(char, end="")
print()
