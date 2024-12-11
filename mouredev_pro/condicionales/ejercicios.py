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
text = input("Introduce una cadena de texto : ")
 
if not text:
    print("La cadena esta vacía")
else:
    print("La cadena no esta vacia")        
#4 Crea un programa que solicite dos números al usuario y compare cual es mayor. si son iguales, muestre un mensaje indicando la igualdad
print("")
print("****** Ejercicio 4 **********")

num1 = int(input("Introduce un primer número: "))
num2 = int(input("introduce un segundo número: "))

if num1 > num2 :
    print(f"{num1} es mayor que {num2}")
elif num1 < num2 :
    print(f"{num1} es menor que {num2}")
else:
    print(f"{num1} es igual a {num2}") 

#5 Escribe un programa que verifique si un número es divisible por 3 y por 5 al mismo tiempo
print("")
print("****** Ejercicio 5 **********")
number = int(input("Introduce un númeromero: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"{number} es divisible por 3 y por 5")
else:
    print(f"{number} no es divisible por 3 y 5 al mismo tiempo") 

# 6. Solicita al usuario que ingrese un número y verifica si es par o impar.
print("")
print("****** Ejercicio 6 **********") 
number = int(input("Introduce un nÃºmero: "))
if number % 2 == 0:
    print(f"{number} es par")
else:
    print(f"{number} es impar")   
 # 7. Escribe un programa que determine si una persona puede votar en función de su edad(mayor o igual a 18). Si tiene 16 o 17 años, indica que puede votar con permiso especial.
print("")
print("****** Ejercicio 7 **********") 

age = int(input("Introduce tu edad: "))
if age >= 18:
    print("Puedes votar")
elif 16 <= age < 18:
    print("Puedes votar con permiso especial")
else:
    print("No puedes votar")
# 8. Crea un programa que solicite una contraseña al usuario y verifique si coincide con una contraseña predefinida. Si no coincide, muestra un mensaje de error.
password = "python123"
user_password = input("Introduce la contraseÃ±a: ")
if user_password == password:
    print("Acceso permitido")
else:
    print("ContraseÃ±a incorrecta")

# 9. Escribe un programa que determine si un número está entre 10 y 20 (ambos incluidos).
number = int(input("Introduce un número: "))
if 10 <= number <= 20:
    print(f"{number} está entre 10 y 20")
else:
    print(f"{number} no está entre 10 y 20")

   
    