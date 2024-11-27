#loops o bucle FOR
#iterar con un objeto.
nombres = ['Antonio','Marcos','Luis','Belen','Jose']

for i  in nombres:
    print("Hola :" + i)
lista = ['a','b','c']
print(" ")
print("***********")
print(" ")
for letra in lista:
    print("letra : " + letra)
print(" ")
print("***********")
print(" ")
print("Recorrer con indice")
lista1 = ["A","B","C","D"]
for i in lista1:
    numero_lista = lista1.index(i) + 1
    print(f"La letra {numero_lista} : {i}")
print(" ")
print("***********")
print(" ")
print("Ejercicio que recorra con la primera letra del un nombre")

nombres1 = ["Antonio","Marcos","Maria","Angela"]
for i in nombres1:
    if i.startswith('A'):
        print(i)
        
