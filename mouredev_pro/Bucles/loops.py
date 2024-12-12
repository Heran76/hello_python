## Bucles - loops
'''
Los bucles nos permiten repetir bloques de código de forma eficiente
evitnado la necesidad de escribir código una y otra vez. En Python. los
bucles son esenciales para trabajar con colecciones de datos y ejecutar tareas
repetitivas de manera rápida y limpia, En esta lección, aprenderemos sobre los dos
tipos principales de bucles en Python: while y for

1.- El bucle while: Este tipo de bucle ejecuta un bloque de código mientras una
condicion sea verdadera. Es ideal cuando no sabemos exactamente cuántas veces se
debe repetir el ciclo, pero tenemos una condición que debe cumplirse para continuar
la ejecución.

2.- El bucle for: Este tipo de bucle se utiliza principalmente para iterar sobre colecciones
de datos, como listas, tuplas, sets y diccionarios, Es perfecto para recorrer cada elemento de una
colección de forma ordenada.
'''

#while
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else :
    print("Mi condición es mayor o igaul que 10")
print(" ")
print("La ejecución continuará")    