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