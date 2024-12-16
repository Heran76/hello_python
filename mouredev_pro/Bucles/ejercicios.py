#ejercicios bucles 
# 1. Usa un bucle while para imprimir los números del 1 al 10.
print(" ")
print("***** Ejercicio 1 *****")
number = 1
while number <= 10:
    print(number)
    number += 1
    # 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
print(" ")
print("***** Ejercicio 2 *****")
my_list = [10,20,30,40,50]
for i in my_list:
        print(i)
# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
print(" ")
print("***** Ejercicio 3 *****")
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)