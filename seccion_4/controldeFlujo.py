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