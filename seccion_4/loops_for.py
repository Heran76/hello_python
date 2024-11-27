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
print("Recorer con indice")
lista1 = ['a','b','c','d','e']
for i in lista1:
    numero_letra = lista1.index(i) + 1
    print(f"letra {numero_letra} : {i}")
    