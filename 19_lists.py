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

# List
friends = ["John", "Jane", "Jack", "Jill", "Jim"]

# Print using for loop
for element in friends:
    print(element)

# Append a new friend
friends.append("Juan")
print(friends)

# Pop a friend
friend = friends.pop(2)
print(friend)

# Remove a friend
friends.remove("Jane")
print(friends)

# Update an element on a list
friends[0] = "Juan"
print(friends)

# Different data types on a list
datos = [25, "Carlos", True, [1, 2, 3]]
print(datos[3][1])
