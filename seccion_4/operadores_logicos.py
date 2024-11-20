#Operadores lógicos. y(and)  o(or) no(not)
'''
Práctica Operadores Lógicos 1
Crea tres variables (num1 ,  num2 y num3):

Dentro de num1, almacena el valor 36

Dentro de num2, almacena el resultado de la operación 72/2

Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, y menor que num3. Almacena el 
resultado de dicha comparación en una variable llamada mi_bool

'''
num11 = 36
num22 = 72/2
num33 = 48
mi_bool = num11 > num22 and num11 < num33
print(mi_bool)
 
'''
Práctica Operadores Lógicos 2
Crea tres variables (num1 ,  num2 y num3):

Dentro de num1, almacena el valor 36

Dentro de num2, almacena el resultado de la operación 72/2

Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, o menor que num3. 
Almacena el resultado de dicha comparación en una variable llamada mi_bool.

'''
num4 = 36
num5 = 72/2
num6 = 48
mi_bool2 = num1 > num2 or num1 < num3
print(mi_bool2)
'''
Práctica Operadores Lógicos 3
Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y

palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

Elon Musk
'''
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"
 
mi_bool = palabra1 not in frase and palabra2 not in frase