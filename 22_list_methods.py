"""
List Methods
Python has a set of built-in methods that you can use on lists.
"""

# append
# Adds a new element to the end of the list.
lista = [1, 2, 3]
lista.append(4)
# print(lista)

# extend
# Extends the list adding all elements from another list.
lista = [1, 2, 3]
lista.extend([4, 5, 6])
# print(lista)

# insert
# Inserts an element in a specific position on the list.
#        0  1  2
lista = [1, 2, 4]
lista.insert(2, 3)
# print(lista)

# Remove
# Removes the first instance found in the list.
# If the element is not found, an error is raised.
lista = [1, 2, 3, 2]
lista.remove(2)
# print(lista)

# pop
# Delete the element in the given icon and return it. If no intice is specified, remove and return the last element.
lista = [1, 2, 3]
elemento = lista.pop(1)
# print(f"Elemento = {elemento}")
# print(lista)

# clear
# Delete all items from the list, leaving it empty.
lista = [1, 2, 3]
lista.clear()
# print(lista)

# index
# Returns the index of the first appearance of the element. A search range can be specified.
lista = [1, 2, 3, 2]
indice = lista.index(2, 2, 4)
# print(indice)


# count
# Returns the number of times the item appears in the list.
lista = [1, 2, 2, 3]
contador = lista.count(2)
# print(contador)


# sort
# Sort the list in place (modify the list). It can be ordered in ascending (default) or descending order if you reverse = True.

lista = [3, 1, 2]
lista.sort(reverse=True, key=lambda item: item)
print(lista)


exit()
# reverse
# Reverse the order of the items in the list.
lista = [1, 2, 3]
lista.reverse()
# print(lista)

# copy
# Returns a superficial copy of the list.
lista = [1, 2, 3]
copia = lista.copy()
lista.append(4)
# print(lista)
# print(copia)

# Bug
lista = [1, 2, 3]
copia = lista
lista.append(4)
print(lista)
print(copia)
