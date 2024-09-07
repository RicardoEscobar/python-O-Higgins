"""
Raw string
Is a string that is prefixed with an r or R. It is used to ignore escape sequences.
"""

normal_string = "Hola\nMundo"
print(normal_string)

raw_string = r"Hola\nMundo"
print(raw_string)

# When to use raw strings?

import re

pattern = r"\d{3}-\d{2}-\d{4}"
match = re.match(pattern, "123-45-6789")

# File system paths
ruta = r'C:\Users\Usuario\Documents'
print(ruta)
