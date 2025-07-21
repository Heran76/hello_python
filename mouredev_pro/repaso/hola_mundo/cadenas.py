'''1. Declara una variable text con la frase “Aprendiendo 
Python” y luego imprime la longitud de la cadena usando 
len()
'''
text="Aprendiendo"
print (len(text))

'''
2. Concatena dos cadenas: “Hola” y “Python”, y muestra el 
resultado en una sola línea
'''
cadena1 = "Hola "
cadena2 = "Python"

print(cadena1+cadena2)

'''
Crea una cadena que incluya un salto de línea, y luego 
imprímela para ver el resultado.
'''
text = "Esta es una caracola \n y esto es otra"
print(text)

'''
4. Usa el formateo de cadenas con f-strings para imprimir 
tu nombre, apellido y edad en una cadena de texto.
'''
name = "Antonio"
surname = "Heredia"
age = 49
print(f"Mi nombre es {name} {surname}  tengo {age} años")

'''
5. Desempaqueta los caracteres de la palabra “Python” en 
variables separadas y luego imprímelos uno por uno.

'''
palabra = "Python"
a, b, c, d, e, f = palabra
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
'''
Extrae un “slice” de la palabra “Programación” para 
obtener los caracteres desde la posición 3 hasta la 7. 
'''
palabra = "Programación"
inicio = 3
fin = 7
slice = palabra[inicio:fin+1]  # Sumamos 1 al final para incluir la posición 7
print(slice)