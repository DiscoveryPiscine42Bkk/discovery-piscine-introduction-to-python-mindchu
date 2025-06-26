#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for element in original_array:
    if element > 5:
        new_array.append(element + 2)
print("Original array:", original_array)
print("New array:", set(new_array))
