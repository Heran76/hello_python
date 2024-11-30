### List ###

my_list = list() #la inicializamos como un variable
my_other_list = []

print(len(my_list)) #longitud de lista nos dice los elementos

my_list = []
#### Ejercicios ####
# 1. Crea una lista con los números del 1 al 5 e imprímela.
my_list = [1,2,3,4,5]
print(my_list)

#2. Accede e imprime el tercer elemento de la lista [10,20,30,40,50]
my_list1 = [10,20,30,40,50]
print(my_list1[2])

#3. Agrega el numero 6 al final de lista [1,2,3,4,5]
my_list2 =[1,2,3,5]
my_list2.append(6)
print(my_list2)

#4 Inserta el número 15 en la posición n2 de lista [10,20,30,40,50]
my_list3 = [10,20,30,40,50]
my_list3.insert(2,15)
print(my_list3)

#5 elimina el primer valor 30 de la lista [10,20,30,40,50]
my_list4 = [10,20,30,30,40,50]
my_list4.remove(30)
print(my_list4)

#6 Usa la función pop() para eliminar el último elemento de la lista [1,2,3,4,5] y almacena en una varialbe. Imprime la variable y la lista
my_lista5 = [1,2,3,4,5]
last_element = my_list.pop()
print(my_lista5)
print(last_element)

# 7 Invierte la lista [100, 200, 300, 400, 500] e imprimela
my_lista7 = [100, 200, 300, 400, 500]
my_lista7.reverse()
print(my_lista7)

# 8 Ordena la lista [3,1,4,2,5] en orden ascendente e imprela
my_lista8 = [3,1,4,2,5]
my_lista8.sort()
print(my_lista8)

# 9 concatena las lista [1, 2, 3] y [4,5,6] y almacena el resultado en una nueva lista, Imprime la lista resultante.
my_lista9 = [1,2,3]
my_lista10 = [4,5,6]
new_lista = my_lista9 + my_lista10
print(new_lista)


#10 Crea una sublista con los elementos de la lista [10,20,30,40,50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3)
my_lista11 = [10,20,30,40,50]
sub_lista = my_lista11[1:3]
print(sub_lista)



