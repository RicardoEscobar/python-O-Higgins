"""
None
Is a special constant in Python that represents the absence of a value or a null value.
"""
# Inicialización de Variables
resultado = None

# Retorno de Funciones
def saludar():
    print("Hola")

# resultado es None porque no se devuelve nada
resultado = saludar()

# Indicador de Valor Faltante o Inexistente
# La edad es desconocida
datos = {"nombre": "Juan", "edad": None}

# Comparación con None
if resultado is None:
    print("No se obtuvo un resultado")
