# 1. Declara una variable text con la frase Aprendiendo Python y luego imprime la longitud de la cadena usando len().

text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: Hola y Python, y muestra el resultado en una sola lÃ­nea.

print("Hola" + " " + "Python")

# 3. Crea una cadena que incluya un salto de lí­nea, y luego imprÃ­mela para ver el resultado.

text = "Esta es una lí­nea\nEsta es otra lí­nea"
print(text)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.

name = "Brais"
surname = "Moure"
age = 37
print(f"Mi nombre es {name} {surname} y tengo {age} aÃ±os")

# 5. Desempaqueta los caracteres de la palabra Python en variables separadas y luego imprÃ­melos uno por uno.

palabra = "Python"
a, b, c, d, e, f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un slice de la palabra Programación para obtener los caracteres desde la posición 3 hasta la 7.

text = "Programación"
text_slice = text[3:8]
print(text_slice)

# 7. Invierte la cadena Pythonusando slicing y muestra el resultado.

text = "Python"
reversed_text = text[::-1]
print(reversed_text)

# 8. Convierte la cadena â€œaprendiendo python en mayúsculas usando el método adecuado e imprímela.

text = "aprendiendo python"
print(text.upper())

# 9. Cuenta cuántas veces aparece la letra n en la cadena Programación en .

text = "Programación en Python"
print(text.count("n"))

# 10. Verifica si la cadena 12345 es numérica usando el método adecuado e imprime el resultado.

text = "12345"
print(text.isnumeric())