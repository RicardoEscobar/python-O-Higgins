"""
Lists
Stores a collection of items in a single variable.
"""
# Several friends
friend1 = "John"
friend2 = "Jane"
friend3 = "Jack"
friend4 = "Jill"
friend5 = "Jim"

# Using Lists
friends = ["John", "Jane", "Jack", "Jill", "Jim"]
print(friends)

# Add a friend to the list
friends.append("Jorge")
print(friends)

# Remove a friend from the list
friends.pop(3)
print(friends)

friends.remove("Jane")
print(friends)

# Modify elements in a list
friends[2] = "Juan"
print(friends)

# Itarate over all elements of a list
for element in friends:
    print(f"My friend is: {element}")

# Different data types on lists
datos = [25, "Carlos", True, [1, 2, 3]]
print(datos[3][1])
