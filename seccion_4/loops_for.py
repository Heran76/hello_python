#loops o bucle FOR
#iterar con un objeto.
nombres = ['Antonio','Marcos','Luis','Belen','Jose']

for i  in nombres:
    print("Hola :" + i)
lista = ['a','b','c']
print(" ")
print("***********")
print(" ")
for letra in lista:
    print("letra : " + letra)
print(" ")
print("***********")
print(" ")
print("Recorrer con indice")
lista1 = ["A","B","C","D"]
for i in lista1:
    numero_lista = lista1.index(i) + 1
    print(f"La letra {numero_lista} : {i}")
print(" ")
print("***********")
print(" ")
print("Ejercicio que recorra con la primera letra del un nombre")

nombres1 = ["Antonio","Marcos","Maria","Angela"]
for i in nombres1:
    if i.startswith('A'):
        print(i)
        
print("*****[ Ejercicios ]*****")

'''
Práctica Loop For 1
Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.

Por ejemplo: "Hola María"

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
'''
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for i in alumnos_clase:
    print("Hola "+ i) 
'''
Práctica Loop For 2
Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
'''    
print(" ")
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros += numero
print("La suma de los números es:", suma_numeros)
'''
Práctica Loop For 3
Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)
'''
print(" ")
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares = 0

# Solo un bucle para recorrer la lista
for num in lista_numeros:
    if num % 2 == 0:  # Verificamos si el número es par
        suma_pares += num
    else:             # Si no es par, es impar
        suma_impares += num

# Imprimir los resultados
print("La suma de los números pares es:", suma_pares)
print("La suma de los números impares es:", suma_impares)