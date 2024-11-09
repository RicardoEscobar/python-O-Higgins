"""
json
Este es un ejemplo de como se puede usar la libreria json para leer y escribir archivos json.
"""
import json


my_dict = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30,
    "casado": False,
    "hijos": None,
    "mascotas": [
        {
            "nombre": "Firulais",
            "edad": 3
        }
    ]
}

# Escribir un archivo json
with open("data1.json", "w") as file:
    json.dump(my_dict, file)

# Leer un archivo json
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)