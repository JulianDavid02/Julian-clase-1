#TABLA DE MULTIPLICAR


# numero = int(input ('Ingrese un número positivo: '))

# if numero > 0:
  
#   for i in range (1, 11):
#      print(numero, "x", i, "=", numero*i)


# else:
#     print("Numero incorrecto, inténtelo de nuevo")    


#SUMA DE NUMERO PARES

# numero = int(input('Ingrese un numero entero: '))

# suma_enteros = 0

# for i in range (2, numero + 1, 2):
#         suma_enteros += i

# print(f"La suma de los número pares desde 2 hasta {numero} es: {suma_enteros}")


#EJERCICIO 3

# lineas = 5 

# for i in range (lineas + 1):
#    print('*' * i)

#CONDICIONALES Y BUCLES

#EJERCICIO 1

num = int(input('ingrese numero'))

suma_pares = 0 

for i in range(1, num + 1):
    if i % 2 == 0:
     suma_pares += i
    print(f'Suma de numeros pares desde 1 hasta {num} es: {suma_pares}')