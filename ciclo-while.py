#EJERCICIO 1

# asce = 0
# desc = 11

# while asce < 10:
#     asce += 1
#     desc -= 1
#     print(asce, '/', desc)


#EJERCICIO 2

import random

aleatorio = random.randint(1, 100)
adivina = 0

while adivina != aleatorio:
    if adivina == 0:
      print("Inicia el juego")
    elif adivina < aleatorio:
       print("demasiado bajo")
    else:
       print("demasiado alto")
    adivina = int(input("Ingresa el numero"))
print("Haz ganado!")   





