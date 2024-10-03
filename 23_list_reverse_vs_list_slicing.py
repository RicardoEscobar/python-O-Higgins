"""
List Patterns
Common patterns when working with lists.
"""

# reverse vs list slicing
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(f"lista: {lista}")

new_lista = lista[::-1]
print(f"new_lista: {new_lista}")
