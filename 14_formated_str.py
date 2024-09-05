"""
Formatted String.
Is a string that has an f at the beginning and curly braces containing expressions that will be replaced with their values.
"""
name = "Luis"
age = 24

# Formatted String
print(f"Hello, my name is {name} and I am {age} years old.")

dog = "Buddy"
dog_age = 3

# Multiline Formatted String
print(f'''My dog's name is {dog}.
He is {dog_age} years old.''')

# Expressions in f-strings
x = 5
y = 10
print(f"La suma de {x} y {y} es {x + y}")

# Number format
pi = 3.14159
print(f"Pi es aproximadamente {pi:.3f}")

# Thousand separator
numero_grande = 1000000
print(f"El número es {numero_grande:,}")

# Date formatting
from datetime import datetime
hoy = datetime.now()
print(f"La fecha de hoy es {hoy:%d/%m/%Y}")

# Text align
print(f"|{'izquierda':<10}|{'centro':^10}|{'derecha':>10}|")

# Complex expressions
x = 21
print(f"El valor es {'par' if x % 2 == 0 else 'impar'}")

# Show {} inside a f-string
print(f"Este es un diccionario: {{'clave': 'valor'}}")

# Final example
nombre = "Ana"
edad = 25
altura = 1.68
saldo_banco = 1234567.89

print(f"""
      Me llamo {nombre}, tengo {edad} años.
      Mido {altura:.2f} metros.
      Y tengo ${saldo_banco:,.2f} en el banco.
""")
