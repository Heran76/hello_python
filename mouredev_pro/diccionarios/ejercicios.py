# 1. Crea un diccionario con las claves name, age, y country, asignando valores a cada una. Imprime el diccionario.

my_dictionay ={"name":"antonio","age":47,"country":"España"}
print(my_dictionay)

# 2. Accede al valor de la clave name en el diccionario.
print(my_dictionay["name"])
# 3. Añde una nueva clave job con el valor "Programador" al diccionario del punto anterior. Imprime el diccionario actualizado.
my_dictionay["job"] = "programador"
print(my_dictionay)
# 4. Modifica el valor de la clave age en el diccionario para que sea 38. Imprime el diccionario actualizado.
my_dictionay["age"] = 48
print(my_dictionay)
# 5. Elimina la clave country del diccionario e imprime el diccionario resultante.
del my_dictionay["country"]
print(my_dictionay)
# 6. Crea un diccionario donde las claves sean números del 1 al 5 y los valores sean sus cuadrados (ejemplo: 1: 1, 2: 4, ...).

# 7. Verifica si la clave age está presente en el diccionario {"name": "Brais", "age": 37, "country": "Galicia"}.

# 8. Imprime solo las claves del diccionario.

# 9. Convierte las claves del diccionario en una lista e imprime la lista resultante.

# 10. Crea un nuevo diccionario a partir de una lista de claves ["name", "age", "job"] usando fromkeys(), asignando a todas las claves el valor "Desconocido".