#funciones.
'''
las funciones son bloques de código reutilizables que nos
permiten organizar nuestro código de manera eficiente, reducir la
repetición y hacerlo mas legible y fácil de mantener.

Las funciones nos permiten dividir grandes programas en pequeñas piezas
manejables facilitando la compresión y el matenimiento de nuestro código
Además nos permiten ejecutar una sentencia de intruciones simplemente llamándolas
por su nombre.
 Las funciones son ensenciales porque te permiten escribir código que es reutilizable
 y modular, En lugar de repetir el mismo codigo una y otra vez, puedes encapsularlo dentro
 de una función y llamarlo siempre que lo necesites. Esto hace que tu programa sea más
 organizado y fácil de entender. Además, las funciones facilitan la depuración y el mantenimiento
 del código a largo plazo.
 '''
 #definición
def separador():
    print(" ")
    print("*******")

def my_fuction(): #se declara con la palabra def
     print("Esto es una función")
separador()
my_fuction()     #se llama así


#función con parámetros de entrada/argumentos.
def sum_two_values(first_values, second_value):
    print(first_values+second_value)
separador()
sum_two_values(40,2)
sum_two_values(10,8)
sum_two_values(20,4) 
sum_two_values("5","7") #aqui concatena dos string
#funciones con parámetros de entrada/argumentos y retono
def sum_two_values_with_return(first_values, second_values):
    my_sum=first_values + second_values
    return my_sum
my_result = sum_two_values_with_return(1.2,5.8)
separador()
print(my_result)
# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Heredia", name="Antonio")
# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default("Antonio", "Heredia")
print_name_with_default("Antonio", "Heredia", "Morante")
# Función con parámetros de entrada/argumentos arbitrarios

my_condition = True
if my_condition: # es lo mismo que if my_condition == True:
    print("Se ejecuta la condición if")


print_upper_texts("Hola", "Python", "Heredia")
print_upper_texts("Hola")