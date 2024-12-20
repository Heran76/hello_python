#Ejercicios funciones#
def separador():
    print(" ")
    print("*******")

# 1. Crea una función llamada "personalized_greeting" que reciba un nombre como argumento e imprima "Hola, <nombre>". Si no se proporciona ningÃºn nombre, debe saludar diciendo "Hola, desconocido".
def personalized_greeting(name="desconocido"):
    print(f"Hola, {name}")
personalized_greeting("Antonio")    
# 2. Escribe una función llamada "multiply" que reciba dos números como argumentos y retorne el resultado de multiplicarlos.
separador()
def multiply(first_number, second_number):
    return first_number * second_number
print(multiply(2, 3))
# 3. Crea una función llamada "is_even" que reciba un número entero como argumento y retorne True si es par y False si es impar.
def is_even(number):
    return number % 2 == 0
separador()
print(is_even(4))
# 4. Escribe una función llamada "convert_to_uppercase" que reciba una cadena de texto y la retorne en mayúsculas.
def convert_to_uppercase(text):
    return text.upper()
separador()
print(convert_to_uppercase("hola"))
# 5. Crea una función llamada "arbitrary_sum" que reciba un número arbitrario de números como argumentos y retorne la suma de todos ellos.
def arbitrary_sum(*numbers):
    return sum(numbers) 
separador()
print(arbitrary_sum(1, 2, 3, 4, 5))
