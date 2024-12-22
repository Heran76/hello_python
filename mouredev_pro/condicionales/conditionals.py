### Conditionals ####
'''
Los condicionales son una de las extructuras en cualquier lenguaje de progrmacion
ya que permiten tomar decisiones basadas en condiciones lógicas. En Python. utilizamos
principalmente la sentencia if, elif y else para controlar el flujo de ejecución
dependiendo de si una condición se cumple o no.

En esta lección, veremos cómo Python evalúa expresiones y ejecuta ciertos bloques de
código en funciones de esasa condiciones.
'''
#if

my_condition = True
if my_condition: # es lo mismo que if my_condition == True:
    print("Se ejecuta la condición if")
 

my_condition = 5 * 2
if my_condition == 10:
    print("Se ejecuta la segunda ejecuión del seguno if")
#if, elif, else

if my_condition > 10 and my_condition < 20 :
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es mayor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continua")  

#Condicional con inspección de valor

my_string = "" #una cadena vacia es igual a False
if not my_string:
    print("Mi cadena de texto es vacía")
if my_string == "Mi cadena de textoooooooo":
    print("Estas cadenas de texto coinciden")                  
    
    
    