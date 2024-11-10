#diccionario
"""
Un diccionario en Python es una estructura de datos que permite almacenar pares de clave-valor. Es similar a un índice o una tabla de búsqueda, donde puedes acceder a los valores usando sus claves en lugar de índices numéricos como en las listas.

Características principales:
Claves únicas: Cada clave debe ser única en el diccionario. Si intentas usar una clave existente, sobrescribirá el valor anterior.
Claves inmutables: Las claves deben ser de un tipo inmutable, como cadenas, números o tuplas.
Valores mutables: Los valores pueden ser de cualquier tipo y pueden cambiarse después de ser asignados.
Sintaxis básica:
Un diccionario se define usando llaves {}.

python
Copiar código
# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor
print(mi_diccionario["nombre"])  # Output: Juan

# Modificar un valor
mi_diccionario["edad"] = 31

# Agregar un nuevo par clave-valor
mi_diccionario["profesión"] = "Ingeniero"

# Eliminar un elemento
del mi_diccionario["ciudad"]

# Recorrer el diccionario
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
Métodos útiles:
keys(): Devuelve las claves.
values(): Devuelve los valores.
items(): Devuelve pares clave-valor.
get(clave, valor_por_defecto): Obtiene un valor sin generar error si la clave no existe.
pop(clave): Elimina un elemento y devuelve su valor.
Ejemplo práctico:

python
Copiar código
# Crear un diccionario vacío
productos = {}

# Añadir elementos
productos["manzana"] = 3
productos["pera"] = 5

# Consultar inventario
print(productos.get("manzana", "No disponible"))  # Output: 3
Los diccionarios son ideales para representar datos estructurados, como un objeto en JSON o una fila en una base de datos.

"""
#Práctica Diccionarios 1
#Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:
#nombre: Karen
#apellido: Jurgens
#edad: 35
#ocupacion: Periodista
#Los nombres de las claves y valores deben ser 
# iguales a la consigna.

mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}
#Práctica Diccionarios 2
#Crea una función print que devuelva del segundo item de la lista llamada points2, 
# dentro del siguiente diccionario.

#Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver
# el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a
# los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict["puntos"]["points2"][1])
