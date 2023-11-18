#EJERCICIO 5 CONDICIONALES

# def evaluar_salario(salario):
#     if salario <= 10000:
#         print('No paga impuestos')
#     elif salario > 10000 and salario < 50000:
#         print('Paga 10% impuestos')  
#     elif salario > 5000 and salario < 100000:
#         print('Paga 20% impuestos')  
#     else:
#         print('Paga 30% de impuestos')   
         
# evaluar_salario(10000)      


#EJERCICIO 10 BUCLES Patron de asteriscos

# def cant_asteriscos(filas):
#     for i in range (1, filas + 1):
#         print('* ' * i)

# cant_asteriscos(5)      


#EJERCICIO 15 CONDICIONALES Y BUCLES

def imprimir_asteriscos(fila):
    for x in range(1, fila + 1):
        if x % 2 == 0:
            print('*' * x)
        else:
            print('+' * x)    
      
imprimir_asteriscos(2)            


     