#tuples
'''
¿Qué es una tupla?
Una tupla es una estructura de datos inmutable en Python que se usa para almacenar múltiples elementos en un solo objeto. Es similar a una lista, pero no se puede modificar después de ser creada. Esto significa que no puedes agregar, eliminar ni cambiar elementos de una tupla.

¿Cómo se crean las tuplas?
Se crean usando paréntesis () o simplemente separando elementos por comas.

python
Copiar código
# Ejemplo de tupla
mi_tupla = (1, 2, 3, 4)

# También puedes crearla sin paréntesis
otra_tupla = 5, 6, 7

# Tupla con un solo elemento (¡atención a la coma!)
tupla_un_elemento = (8,)
Características principales de las tuplas
Inmutables: No puedes cambiar sus elementos después de crearlas.
Ordenadas: Los elementos tienen un orden fijo y se pueden acceder por índice.
Pueden contener diferentes tipos de datos: Una tupla puede tener enteros, cadenas, flotantes, etc.
python
Copiar código
mi_tupla = (1, "Hola", 3.14, True)
Acceder a elementos
Usa los índices (comenzando desde 0) para acceder a los elementos:

python
Copiar código
mi_tupla = (10, 20, 30, 40)
print(mi_tupla[1])  # Imprime 20
Ventajas de las tuplas
Más rápidas que las listas: Como son inmutables, Python las procesa más rápido.
Seguras: Al ser inmutables, puedes usarlas para datos que no deben cambiar.
Se pueden usar como claves de diccionarios: Debido a que son inmutables, son "hashables".
Métodos de las tuplas
Como son inmutables, tienen pocos métodos. Los más usados son:

count(): Cuenta cuántas veces aparece un elemento.
index(): Devuelve el índice de la primera aparición de un elemento.
python
Copiar código
mi_tupla = (1, 2, 3, 1, 2, 1)
print(mi_tupla.count(1))  # Imprime 3
print(mi_tupla.index(2))  # Imprime 1
Ejemplo práctico
Usa tuplas para representar coordenadas (x, y) o datos que no cambiarán, como los días de la semana.

python
Copiar código
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
print(dias_semana[0])  # Imprime 'Lunes'
Resumen
Las tuplas son como listas, pero no se pueden modificar.
Se usan para datos que deben permanecer constantes.
Son rápidas y seguras para ciertos tipos de tareas.
'''
#Práctica Tuples 1
#Utiliza un método de tuplas para contar la cantidad
# de veces que aparece el valor 2 en la siguiente 
# tupla, y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#Práctica Tuples 2
#Convierte a lista la siguiente tupla, y almacénala en una 
# variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)
print(type(mi_lista))

#Práctica Tuples 3
#Extrae los elementos de la siguiente tupla en 
#cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla
print(a)