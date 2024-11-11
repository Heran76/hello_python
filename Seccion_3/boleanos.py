#Boleanos (bool)
'''
En Python, un valor booleano es un tipo de dato que puede tener solo dos valores: True o False. Estos valores se utilizan para representar estados lógicos o resultados de comparaciones y operaciones condicionales.

Características clave:
Son parte del tipo de datos bool.
Se utilizan principalmente en estructuras de control como if, while y expresiones lógicas.
En evaluaciones, muchos valores son tratados como booleanos:
False: 0, cadenas vacías "", listas vacías [], diccionarios vacíos {}, y None.
True: Cualquier otro valor.
Ejemplo:
python
Copiar código
# Ejemplo de comparación
x = 10
y = 20
resultado = x < y  # Esto devuelve True

# Uso en una condición
if resultado:
    print("x es menor que y")
else:
    print("x no es menor que y")
El tipo booleano es fundamental en la programación para el control de flujo y toma de decisiones.

'''
#Práctica Booleanos 1
#Realiza una comparación que arroje como resultado 
#un booleano y almacena el resultado (True/False) en 
#variable llamada prueba.

prueba = 5 >= 8;
print(type(prueba)) 