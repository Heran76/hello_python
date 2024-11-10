#Set
'''
set es una colección desordenada de elementos únicos. Es útil cuando necesitas almacenar elementos sin duplicados y realizar operaciones matemáticas como unión, intersección y diferencia.

Características principales:
Elementos únicos: No permite duplicados. Si agregas un elemento repetido, solo se almacena una copia.
No ordenado: Los elementos no tienen un índice, por lo que no puedes acceder a ellos por posición.
Mutables: Puedes agregar o eliminar elementos después de crear el set.
Tipos inmutables: Los elementos dentro de un set deben ser inmutables, como números, cadenas o tuplas.
Ejemplo básico:
python
Copiar código
# Crear un set
mi_set = {1, 2, 3, 4, 4}
print(mi_set)  # Salida: {1, 2, 3, 4}

# Agregar elementos
mi_set.add(5)
print(mi_set)  # Salida: {1, 2, 3, 4, 5}

# Eliminar elementos
mi_set.remove(3)
print(mi_set)  # Salida: {1, 2, 4, 5}

# Verificar si un elemento está en el set
print(2 in mi_set)  # Salida: True
Operaciones útiles:
Unión: Combina los elementos de dos sets.

python
Copiar código
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Salida: {1, 2, 3, 4, 5}
Intersección: Encuentra los elementos comunes.

python
Copiar código
print(set1 & set2)  # Salida: {3}
Diferencia: Elementos en un set pero no en el otro.

python
Copiar código
print(set1 - set2)  # Salida: {1, 2}
Diferencia simétrica: Elementos que están en uno u otro, pero no en ambos.

python
Copiar código
print(set1 ^ set2)  # Salida: {1, 2, 4, 5}
Creación con set():
Puedes crear sets vacíos o convertir otros iterables en sets:

python
Copiar código
set_vacio = set()  # Set vacío
mi_set = set([1, 2, 2, 3])  # Salida: {1, 2, 3}
Los sets son ideales para eliminar duplicados de listas o trabajar con operaciones matemáticas.
'''
#Práctica Sets 1
#Une los siguientes sets en uno solo, llamado
# mi_set_3:
mi_set1={1, 2, "tres", "cuatro"}
mi_set2={"tres", 4, 5}
mi_set3=mi_set1.union(mi_set2)
print(mi_set3)

#Práctica Sets 2
#Elimina un elemento al azar del siguiente set, 
# utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}