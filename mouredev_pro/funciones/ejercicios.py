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
# 6. Escribe una función llamada "generate_full_greeting" que reciba dos argumentos: nombre y apellido, y retorne el saludo completo "Hola, <nombre> <apellido>". Los argumentos deben ser pasados por clave.
def generate_full_greeting(name, surname):
    return f"Hola, {name} {surname}" 
separador()
print(generate_full_greeting(name="Antonio", surname="Heredia"))
# 7. Crea una función llamada "power" que reciba dos números: base y exponente, y retorne el resultado de elevar la base al exponente.
def power(base, exponent):
    return base ** exponent
separador()
print(power(2, 3))
# 8. Escribe una función llamada "calculate_average" que reciba tres números y retorne su promedio.
def calculate_average(number1, number2, number3):
    return (number1 + number2 + number3) / 3    
separador()
print(calculate_average(2, 4, 6))
# 9. Crea una funcion llamada "count_characters" que reciba una cadena de texto y retorne el número de caracteres que contiene.
def count_characters(text):
    return len(text)    
separador()
print(count_characters("Hola"))
# 10. Escribe una función llamada "display_messages" que reciba un nÃºmero indefinido de cadenas y las imprima en mayúculas, una por una, tal como se hizo en el archivo proporcionado.
def display_messages(*texts):
    for text in texts:
        print(text.upper()) 
separador()
display_messages("Hola", "Python", "Heredia")