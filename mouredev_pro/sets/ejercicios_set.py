# 1. Crea un set con los números del 1 al 5 e imprí­melo.

my_set = {1,2,3,4,5}
print(my_set)

# 2. Añade el número 6 al set {1, 2, 3, 4, 5} e imprí­melo.
my_set ={1,2,3,4,5}
my_set.add(6)
print(my_set)
# 3. Intenta añadir el número 5 al set {1, 2, 3, 4, 5} nuevamente. ¿Qué sucede?
my_set = {1, 2, 3, 4, 5}
my_set.add(5)
# Salida: {1, 2, 3, 4, 5} (no cambia porque los sets no admiten duplicados)
print(my_set)

# 4. Verifica si el número 3 está en el set {1, 2, 3, 4, 5} e imprime el resultado.
print(3 in my_set)

# 5. Elimina el número 4 del set {1, 2, 3, 4, 5} e imprime el set resultante.
my_set.remove(4)
print(my_set)

# 6. Usa el mÃ©todo clear() para vaciar un set y luego imprime su longitud.

# 7. Convierte el set {"manzana", "naranja", "plÃ¡tano"} en una lista e imprime el primer elemento de la lista.

# 8. Realiza la uniÃ³n de dos sets: {1, 2, 3} y {4, 5, 6}, e imprime el set resultante.

# 9. Calcula la diferencia entre los sets {1, 2, 3, 4} y {3, 4, 5, 6} e imprime el resultado.

# 10. Elimina un set llamado my_set usando del y luego intenta imprimirlo para ver el resultado