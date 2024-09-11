"""
Type conversion
Is the process of converting the value of one data type (integer, string, float, etc.) to another data type.
"""

# Implicit conversion
x = 10    # int
y = 3.5   # float

# Implicit conversion of x from int to float for the operation
z = x + y

print(z)  # 13.5
print(type(z))  # <class 'float'>

# Explicit conversion
# int(): Converts a value to an integer.
# float(): Converts a value to a float.
# str(): Converts a value to a string.
# list(): Converts an iterable to the list type.
# tuple(): Converts an iterable to the tuple type.
# set(): Converts an iterable to the set type.

# From float to int
a = 7.8
b = int(a)
print(f"From float: {a} to int: {b}")

# From int to float
c = 3
d = float(c)  # 3.0
print(f"From int: {c} to float: {d}")

# From int to string
e = 42
f = str(e)  # "42"
print(f"From int: {e} to string: {f}")

# From string to int
g = "100"
h = int(g)  # 100
print(f"From string: {g} to int: {h}")

# From string to float
i = "100.9"
j = str(i)  # 100.9
print(f"From str: {i} to float: {j}")




# From list to tuple
i = [1, 2, 3]
j = tuple(i)
print(f"From list: {i} to tuple: {j}")

# From tuple to list
k = (1, 2, 3, 4)
l = list(k)
print(f"From tuple: {k} to list: {l}")

# From list to set
m = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
n = set(m)
print(f"From list: {m} to set: {n}")

# From tuple to set
h = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)
i = set(h)
print(f"From tuple: {h} to set: {i}")





# Consideration
k = "hello"
l = int(k)
