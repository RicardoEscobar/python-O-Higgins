"""
List slicing
Is a feature in Python that allows you to extract a subset of a list.
"""

# Negative indexes
#         -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last_3 = numbers[::-3]
print(last_3)

# Slice a list
# Syntax: list[start:stop:step]
# start: The starting index of the slice.
# stop: The ending index of the slice.
# step: The step value of the slice.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
slice = numbers[2:5]
print(slice)  # Output: [3, 4, 5]

# Slice with step
slice = numbers[0:10:2]
print(slice)  # Output: [1, 3, 5, 7, 9]

# Slice with negative step
slice = numbers[10:0:-2]
print(slice)  # Output: [10, 8, 6, 4, 2]

# Slice with negative start
slice = numbers[-10:5]
print(slice)  # Output: [1, 2, 3, 4, 5]

# Slice with negative stop
slice = numbers[5:-1]
print(slice)  # Output: [6, 7, 8, 9]

# Slice with negative start and stop
slice = numbers[-10:-1]
print(slice)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slice with negative start and stop and step
slice = numbers[-10:-1:2]
print(slice)  # Output: [1, 3, 5, 7, 9]

# Slice with negative start and stop and negative step
slice = numbers[-1:-10:-2]
print(slice)  # Output: [10, 8, 6, 4, 2]
