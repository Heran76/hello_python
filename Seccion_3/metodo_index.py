#Métedo index()
#saber que posicion de encuentra un carácter
#conocer qué caracter se encuentra [] 
#el indice es sensible a mayusculas
#en caracteres repetidos nos dice le primer caracter que encuentra y busca de izquierda a derecha

mi_texto = "Esta es una prueba";
resultado = mi_texto[9];
resultado2 = mi_texto.index("n");

print(resultado);
print(resultado2);

#Práctica Método Index() 1
#Encuentra y muestra en pantalla qué caracter ocupa la quinta 
#posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[4])

#Práctica Método Index() 2
#Encuentra y muestra en pantalla el índice de la primera aparición
# de la palabra "práctica" en la siguiente frase:

#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))

#Práctica Método Index() 3
#Encuentra y muestra en pantalla el índice de la última 
# aparición de la palabra "práctica" en la siguiente frase:

#"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.rindex("práctica"))