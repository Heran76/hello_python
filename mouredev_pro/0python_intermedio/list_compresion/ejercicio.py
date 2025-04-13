# 1. Genera una lista utilizando comprensión con los números del 0 al 10.

números = [i para i en rango(11)]
print(números)

# 2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.

cuadrados = [i**2 para i en el rango (1, 11)]
print(cuadrados)

# 3. Genera una lista utilizando comprensión con los números pares del 0 al 20.

par = [i para i en rango(21) si i % 2 == 0]
print(par)

# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.

grados centígrados = [0, 10, 20, 30, 40]
Fahrenheit = [(temp * 9/5) + 32 para la temperatura en grados Celsius]
print(fahrenheit)

# 5. Crea una lista utilizando la comprensión con los caracteres de una cadena.

texto = "Python"
caracteres = [carácter por carácter en el texto]
imprimir(caracteres)

# 6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.

palabras = ["brais", "moure", "dev", "hola", "python"]
grande = [p para p en palabras si len(p) > 4]
print(grande)

# 7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.


def suma_cinco(n):
    return n + 5


números = [1, 2, 3, 4, 5]
resultado = [suma_cinco(n) para n en números]
imprimir(resultado)

# 8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.

números = [2, 15, 9, 42, 3]
mayor = [n > 10 para n en números]
imprimir(mayor)

# 9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.

números = [1, 2, 3, 4, 5, 6]
probabilidades_divisibles_por_3 = [n * 3 para n en números si n % 2 != 0]
imprimir(probabilidad_divisible_por_3)

# 10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.

matriz = [[fila * 3 + columna + 1 para columna en rango(3)] para fila en rango(3)]
imprimir(matriz)