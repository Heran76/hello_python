'''
Realiza las siguientes operaciones aritméticas: 
Suma: 15 + 25 
Resta: 50 - 22 
Multiplicación: 8 * 7 
División: 100 / 20 
'''
suma = 15 + 25
resta = 50 - 22
multiplicacion = 8*7
division = 100 / 20
print("*****ejecicio1*****")
print(suma)
print(resta)
print(multiplicacion)
print(division)

'''
2. Calcula el resto de la división de 37 entre 5 y 
almacénalo en una variable remainder. Luego imprímelo.
'''
print("*****ejecicio2*****")
remainder = 37%5
print(remainder)

'''
Convierte el número 7 en una cadena de texto y 
concaténalo con la frase “ es mi número favorito”. 
Imprime el resultado.
'''
numero = 7
print("es mi numero favorito",str(numero))

'''
Repite la palabra “Python” 10 veces usando el operador 
de multiplicación para cadenas y luego imprímela.
'''
word = "python ,"*10
print(word)

'''
5. Crea dos variables: a y b con los valores 12 y 8 
respectivamente. Compara si a es mayor que b y almacena 
el resultado en una variable booleana resultado. Imprime 
el valor de resultado.
'''
a = 12
b = 8
result = a > b
print(result)
'''
Compara dos cadenas de texto (“apple” y “banana”) usando 
los operadores > y < y explica cuál tiene mayor orden 
alfabético

'''
print("apple" > "banana")
print("apple" < "banana")

'''
7. Realiza una comparación lógica usando and para verificar 
si el número 10 es mayor que 5 y menor que 20. Imprime 
el resultado.
'''

print(10 > 5 and 10 < 20)

'''
Usa el operador or para verificar si el número 7 es 
menor que 3 o mayor que 5. Imprime el resultado
'''
print(7 <3 or 7>5)

'''
# 9. Aplica el operador not para invertir el resultado de la comparaciÃ³n 15 > 20. Â¿CuÃ¡l es el resultado?
'''
print(not (15 > 20))
