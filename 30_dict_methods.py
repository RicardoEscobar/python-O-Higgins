"""
dict methods
Here is a list of all the methods that are available with the dictionary objects.
"""

# clear() - Removes all the elements from the dictionary
my_dict = {'name': 'Jack', 'age': 26}
my_dict.clear()
print(my_dict)

# copy() - Returns a copy of the dictionary
my_dict = {'name': 'Jack', 'age': 26}
new_dict = my_dict.copy()
print(new_dict)

# fromkeys() - Returns a dictionary with the specified keys and values
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# get() - Returns the value of the specified key
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.get('name'))

# items() - Returns a list containing a tuple for each key value pair
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.items())

# keys() - Returns a list containing the dictionary's keys\
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.keys())

# pop() - Removes the element with the specified key
my_dict = {'name': 'Jack', 'age': 26}
my_dict.pop('name')
print(my_dict)

# popitem() - Removes the last inserted key-value pair
my_dict = {'name': 'Jack', 'age': 26}
my_dict.popitem()
print(my_dict)

# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.setdefault('name', 'default'))
print(my_dict.setdefault('name1', 'default'))

# update() - Updates the dictionary with the specified key-value pairs
my_dict = {'name': 'Jack', 'age': 26}
my_dict.update({'name': 'Jill'})
print(my_dict)

# values() - Returns a list of all the values in the dictionary
my_dict = {'name': 'Jack', 'age': 26}
print(my_dict.values())
