"""
List Patterns
Common patterns when working with lists.
"""

# Join with spaces
palabras = ['Hola', 'mundo', 'Python']
frase = ' '.join(palabras)
# print(frase)

# Join with custom separator
palabras = ['Hola', 'mundo', 'Python']
frase = '-'.join(palabras)
# print(frase)

# Join with empty list
lista_vacia = []
resultado = ','.join(lista_vacia)
# print(resultado)

# Error when not a str
lista_vacia = [1, 2, 3]
resultado = ','.join(lista_vacia)
print(resultado)

