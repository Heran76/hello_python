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
# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
print(" ")
print("***** Ejercicio 4 *****")
word = "Python"
for letter in word:
    print(letter)

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
print(" ")
print("***** Ejercicio 5 *****")
i = 1
while i <= 50:
    if i % 7 == 0:
        print(i)
        break
    i += 1 
  # 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
print(" ")
print("***** Ejercicio 6 *****")  
person = {"name": "Brais", "age": 37, "country": "Galicia"}
for key in person:
    print(key)   

   # 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20. 
print(" ")
print("***** Ejercicio 7 *****") 
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1