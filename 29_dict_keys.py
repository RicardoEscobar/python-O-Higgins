"""
Dictionary keys
A dictionary key must be of a type that is immutable. This means that you can use strings, numbers or tuples as dictionary keys but something like a list is not allowed.
"""
my_dict = {
    "uno": 1,
    "uno": 2,
    2: "dos",
    3.3: "tres",
    True: "cuatro",
    True: "Remplazo",
    False: "cinco",
    (1,2,3): "seis",
}
print(my_dict)