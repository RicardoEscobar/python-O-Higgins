"""
Variables are used to store data values.
"""

x = 5
name = "Ana"
pi = 3.14
is_valid = True
friend_list = ["Ana", "Juan", "Pedro"]
friend_tuple = ("Ana", "Juan", "Pedro")
friend_set = {"Ana", "Juan", "Pedro"}
friend_dict = {"name": "Ana", "age": 24}

# Value change
x = 10
print(x) # 10

x = 20
print(x) # 20

# Variable names
# A variable name must start with a letter or the underscore character
x = 10
name = "Ricardo"
_variable = True

# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# Best practices
# Use meaningful names
# Use lowercase for variable names
# Use underscore to separate words
# Avoid using special characters
# Avoid using keywords
# Avoid using built-in functions

# Constants
# Constants are variables that are not supposed to change.
PI = 3.14
SERVER = "http://localhost:8080"
DB_NAME = "my_database"

# The _ character is used to indicate that a variable is private
_name = "Ricardo"
_age = 24
_is_valid = True

# _ is also used to indicate that a variable is temporary or insignificant
_ = 0
for _ in range(10):
    print(_) # 0 1 2 3 4 5 6 7 8 9