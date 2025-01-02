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
# 3. Crea una función que abra un archivo, lea su contenido y maneje posibles errores (por ejemplo, archivo no encontrado). Usa try-except para gestionar las operaciones de archivos de forma segura.

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: Fichero no encontrado.")        
 # 4. Crea una función que realice múltiples operaciones (suma, resta, divisiÃ³n, multiplicación) con dos números. Usa try-except-else-finally para manejar errores y asegurar que se imprima un mensaje final, independientemente de los errores.

def perform_operations(num1, num2):
    try:
        print(f"Suma: {num1 + num2}")
        print(f"Resta: {num1 - num2}")
        print(f"MultiplicaciÃ³n: {num1 * num2}")
        print(f"DivisiÃ³n: {num1 / num2}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print("Operaciones realizadas correctamente.")
    finally:
        print("Fin de las operaciones.")       
      