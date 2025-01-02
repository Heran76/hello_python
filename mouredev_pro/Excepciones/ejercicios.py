#Ejercicios Excepciones##
# 1. Crea una función que intente dividir dos números proporcionados por el usuario. Usa try-except para capturar cualquier error de división (por ejemplo, división por cero).

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"El resultado es {result}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")