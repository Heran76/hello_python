#Propiedades string.
#inmutable no podemos cambia su contendio solo se hace aplicando con otra variable
#concatenar
# (*) se pueden multiplicar
# multilinea con tres comillas dobles

#Práctica Propiedades de Strings 1
#Concatena 15 veces el texto "Repetición" y muestra el 
#resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de 
#forma simple y elegante.

palabra = "Repetición"
 
print(palabra * 15)

#Práctica Propiedades de Strings 2
#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

#Tierra mojada,

#mis recuerdos de viaje

#entre las lluvias
haiku = '''
Tierra mojada
mis recuerdos de viaje,
entre las lluvias
'''
 
print("agua" not in haiku)

#Práctica Propiedades de Strings 3
#Muestra en pantalla el largo (en números de caracteres) de 
# la palabra electroencefalografista.

palabra = "electroencefalografista"
 
print(len(palabra))
