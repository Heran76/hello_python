#Ejercicios Excepciones##
# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"El resultado es {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
# 2. Crea una función que tome una cadena e intente convertirla en un número entero. Usa try-except para capturar cualquier error en la conversión.

def convert_to_integer(string):
    try:
        return int(string)
    except ValueError:
        print("Error: No se puede transformar a entero.")
      