import sys
import time
'''Declara y asigna valores a las siguientes variables: 
name: una cadena que contenga tu nombre. 
age: un número entero que represente tu edad. 
height: un número flotante que represente tu altura. 
Imprime cada variable en una línea separada.?'''

names="Antonio"
age=48
height=1.85
print(names)
print(age)
print(height)

# Convierte la variable edad de entero a cadena y 
#concatenala con un texto que diga cuántos años tienes
print("tengo "+str(age)+" años")

'''Declara una variable booleana is_student que indique si 
eres estudiante o no. Usa True o False según corresponda 
e imprímela.'''

is_student = True
print(is_student)

'''
Usa la función len() para calcular cuántos caracteres 
tiene tu nombre completo, almacenado en una variable.

'''

name = "Antonio"
print("EL nombre antonio tiene",len(name)," palabras")

'''
Declara tres variables en una sola línea que representen 
tu nombre, apellido y ciudad de origen. Luego, imprime 
estos valores.
'''
name, surname, city = "Antonio", "heredia", "huesa"
print(name, surname, city)

'''
Usa la función input() para solicitar al usuario su 
color favorito y almacénalo en una variable color. 
Luego, imprime el valor ingresado.

'''

color = input("Escribe tu color favorito")
print("mi color faborito es : ", color)

'''
 Declara una variable fruit e inicialízala con un valor. 
Luego, cambia el valor de la fruta a otro diferente y 
vuelve a imprimirla.

'''
fruit = "naranja"
print(fruit)
fruit = 'fresa'
print(fruit)

'''
Convierte un número decimal, almacenado en la variable 
price, a un número entero y luego imprímelo.
'''
print("*****Número entero******")
price = 48.72
print(int(price))
'''
Declara una variable llamada address_len y almacena en 
ella la cantidad de caracteres de una dirección usando 
la función len(). Imprime el resultado.
'''
print("****Len()****")
address = "Calle Palas de rey"
address_len = len(address)
print(address_len)

'''
10. Usa un tipo de dato forzado para declarar una 
variable phone, asegurándote de que siempre será un 
número. Luego, cambia su valor a un número diferente y 
verifica el tipo de la variable con type(). 
'''
phone: int = 123456789
print(type(phone))
phone = 600956956
print(type(phone))
