#condiciones de flujo
'''
El control de flujo en Python es la forma en que un programa decide qué instrucciones ejecutar y en qué orden, según ciertas condiciones o estructuras. Esto permite que el programa sea dinámico y pueda adaptarse a diferentes situaciones. Las principales herramientas de control de flujo en Python son:

1. Condicionales (if, elif, else)
Permiten ejecutar bloques de código basados en condiciones.

python
Copiar código
x = 10
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
2. Bucles (for, while)
Permiten repetir bloques de código varias veces.

for loop: Itera sobre una secuencia como listas, cadenas o rangos.
python
Copiar código
for i in range(3):
    print(i)  # Imprime 0, 1, 2
while loop: Repite el bloque de código mientras la condición sea verdadera.
python
Copiar código
count = 0
while count < 3:
    print(count)
    count += 1
3. Declaraciones de control dentro de bucles (break, continue, pass)
break: Sale del bucle inmediatamente.
continue: Salta a la siguiente iteración del bucle.
pass: No hace nada; sirve como un marcador de posición.
python
Copiar código
for i in range(5):
    if i == 3:
        break  # Termina el bucle cuando i es 3
    if i == 2:
        continue  # Salta la iteración cuando i es 2
    print(i)

# pass ejemplo
if True:
    pass  # Placeholder para implementar después
4. Comprensiones (List, Set, Dict Comprehensions)
Una forma concisa de manejar estructuras con control de flujo dentro.

python
Copiar código
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers if n % 2 == 0]
print(squared)  # [4, 16]
'''

'''
Práctica Control de Flujo 1
Utilizando las variables num1 y num2, que se alimentan con 
input del usuario (tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los valores
de las variables, y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2"

"num2 es mayor que num1"

"num1 y num2 son iguales"

Debes mostrar en pantalla el valor de las variables 
ingresadas en lugar de num1 y num2.

Aclaración:

1. No deben imprimirse strings adicionales a la respuesta del
usuario.

2. Los ejercicios que contienen el la función input() deben ser probados con el botón: "Ejecutar pruebas".  Ya que el botón "Ecutar código" arrojará el siguiente error: "EOF when reading a line".
'''
num1 = int(input("Ingresa un número:"))
num2 = int(input("Ingresa otro número:"))
 
if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num2 > num1:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")
'''
Práctica Control de Flujo 2
Las leyes de un país establecen que un adulto puede conducir si tiene licencia
para hacerlo, y para optar por una licencia para conducir, debe de tener 18 años o más.

Crea una estructura condicional para verificar si una persona 
de 16 años sin licencia puede conducir, y muestra el resultado que corresponda en pantalla:

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones.

'''    
edad = 16
tiene_licencia = False

"Puedes conducir"

"No puedes conducir aún. Debes tener 18 años y contar con una licencia"

"No puedes conducir. Necesitas contar con una licencia"

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

'''
Práctica Control de Flujo 3
Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

Utiliza la base de código ya proporcionada para plantear la estructura de control de flujo apropiada y verificar dichas condiciones. Evalúa a un candidato que sabe inglés, pero no programa en Python.

'''    
habla_ingles = True
sabe_python = False

"Cumples con los requisitos para postularte"

"Para postularte, necesitas saber programar en Python y tener conocimientos de inglés"

"Para postularte, necesitas tener conocimientos de inglés"

"Para postularte, necesitas saber programar en Python"

if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte")
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")