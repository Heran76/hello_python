#Módulos#
'''
En Python, modular se refiere a la capacidad de dividir el código
en partes más pequeñas y manejables llamadas módulos.
Un módulo es simplemente un archivo de Python que contiene definiciones y declaraciones, como 
funciones, clases o variables, que pueden ser reutilizadas en otros archivos o proyectos. Esto fomenta la reusabilidad, organización y mantenimiento
del código.
'''


from math import pi as PI_VALUE
import math
from my_module import sumValue, printValue
import my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


sumValue(5, 3, 1)
printValue("Hola python")


print(math.pi)
print(math.pow(2, 8))


print(PI_VALUE)