#!/usr/bin/env python3

first_num = input("Give me the first number: ")
second_num = input("Give me the second number: ")
try:
    first_num = int(first_num)
    second_num = int(second_num)
    print("Thank you!")
    print(f"{first_num} + {second_num} = {first_num + second_num}")
    print(f"{first_num} - {second_num} = {first_num - second_num}")
    print(f"{first_num} / {second_num} = {int(first_num / second_num)}")
    print(f"{first_num} * {second_num} = {first_num * second_num}")
except:
    print("Invalid input")
