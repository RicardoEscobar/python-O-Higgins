"""
Strings are immutable sequences of characters.
Strings are enclosed in single quotes ('...')
or double quotes ("...") with the same result.
"""
# Example using double quotes ("...")
cadena1 = "Mundo"

# Example using single quotes ('...')
cadena2 = 'Hola'

# Example mixing single and double quotes
cadena3 = "Hola 'Mundo'"
print(cadena3)

cadena4 = 'Hola "Mundo"'
print(cadena4)

# Example using escape characters
cadena5 = "My name is Jorge, I\'m a \"programmer\"."
print(cadena5)

# Multi-line str
cadena_multilinea = """Hola, mundo.
Esto es nuevo.
Esto tambien es nuevo."""
print(cadena_multilinea)

# Inmutable str
cadena = "Hola"
# cadena[0] = 'h'  # Esto generaría un error

# Concatenate str
saludo = "Hola" + " " + "Mundo"
print(saludo)

# Repeat str
repeticion = "Hola " * 3
print(repeticion)

# Element access
cadena = "Python"

print(cadena[0])  # P
print(cadena[-1])  # n (último carácter)

# Common methods
cadena = "  Python is hard very powerful.  "
print(len(cadena))
print(cadena.upper())
print(cadena.lower())
print(cadena.strip())
print(cadena.replace("hard", "easy and"))
print(cadena.split(" "))
print(cadena.find("hard"))

# Combining methods
print(cadena.strip().upper())

# Is a substring in a string?
print("hard" in cadena)

# Formatted strings
nombre = "Jorge"
edad = 24

print(f"Hola, me llamo {nombre} y tengo {edad} años.")

# Don't use this
print("Hola, me llamo " + nombre + " y tengo " + str(edad) + " años.")

# Formatted strings with expressions
print(f"El doble de mi edad es {edad * 2}.")

# Formatted strings with multiline strings
nombre = "Jorge"
edad = 24
saludo = f"""Hola, me llamo {nombre}
y tengo {edad} años."""

# Raw strings
# cadena_fail = "C:\Users\Jorge\Documents"
# print(cadena_fail)

cadena = r"C:\Users\Jorge\Documents"
print(cadena)

# Raw strings with multiline strings
cadena = r"""C:\Users\Jorge\Documents
C:\Users\Jorge\Downloads"""
print(cadena)
