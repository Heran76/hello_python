# Ejercicios Condicionales
# 1. Escribe un programa que verifique si un número es positivo, negativo o cero.
print("")
print("****** Ejercicio 1 **********")
number = int(input("Introduce un número : ")) 

if number > 0 :
    print("El numero introducido es positivo")
elif number < 0 :
    print ("El número introducido es negativo")
else :
    print("El numero introducio es igual a 0")   

## 2. Solicita al usuario que ingrese su edad y muestra un mensaje indicando si es mayor de edad(18 años o mas) o menor de edad.
print("")
print("****** Ejercicio 2 **********")  

age = int(input("Introduce tu edad : "))
if age >= 18 :
    print("Eres mayor de edad")
else : 
    print("Eres menor de edad") 

#3 Escribe un programa que verifique si una cadena de texto está vacia y muestra un mensaje en consecuencia
print("")
print("****** Ejercicio 3 **********")
text = input(input("Introduce una cadena de texto : "))  
if not text:
    print("La cadena esta vacía")
else:
    print("La cadena no esta vacia")        
