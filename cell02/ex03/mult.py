#!/usr/bin/env python3

first_num = input("Enter the first number:\n")
second_num = input("Enter the second number:\n")
try:
    first_num = int(first_num)
    second_num = int(second_num)
    ans = first_num * second_num
    print(f"{first_num} x {second_num} = {ans}")
    if ans < 0:
        print("The result is negative.")
    elif ans > 0:
        print("The result is positive.")
    elif ans == 0:
        print("The result is positive and negative.")
except:
    print("Invalid input.")
