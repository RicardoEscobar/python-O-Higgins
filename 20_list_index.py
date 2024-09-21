"""
List Index
The index is used to access or refer to an element in a list.
"""

# Positive indexing
# indexes: 0  1  2  3  4
numbers = [1, 2, 3, 4, 5]

# Negative indexing
#           -3         -2         -1
lista = ['manzana', 'banana', 'cereza']
print(lista[-1])
print(lista[-2])

# Index error
#           0          1         2          3?
lista = ['manzana', 'banana', 'cereza']
# print(lista[3])

# Update list items
lista = ['manzana', 'banana', 'cereza']
#           0           1         2
print(lista)
lista[1] = 'naranja'
print(lista)
