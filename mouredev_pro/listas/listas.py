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