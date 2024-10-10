# while True:
#     print("I'm stuck in an infinite loop!")

# counter = 0
# while counter < 5:
#     print(f"This loop ran {counter + 1} times!")
#     counter += 1

# import random

# respuesta = random.randint(1, 10)
# intentos = 0
# while True:
#     intentos += 1
#     try:
#         guess = int(input("Adivina un numero del 1 al 10: "))

#         if guess == respuesta:
#             print(f"Adivinaste! en {intentos} intentos.")
#             break
#         else:
#             if guess < respuesta:
#                 print("Muy bajo")
#             else:
#                 print("Muy alto")
            
#             print("Intenta de nuevo")

#     except ValueError:
#         print("Por favor ingresa un numero valido")
#         continue

# print("Fin del juego")

try:
    num = int(input("Dame un numero: "))
except ValueError:
    print("Por favor ingresa un numero valido")
    exit()

print(num + 1)
print(type(num))