"""
dict
A data structure that stores data as key-value pairs.
"""

# Ejemplo de un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "Ingeniero"
}

# Acceder a valores
print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])

# Modificar valores
mi_diccionario["nombre"] = "Luis"
mi_diccionario["edad"] = 25

print(mi_diccionario["nombre"])
print(mi_diccionario["edad"])

# Comprobación de claves
print("nombre" in mi_diccionario)
print("zzzz" in mi_diccionario)
