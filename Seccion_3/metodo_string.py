#Metodo string
#upper()- pasa a mayusculas
#lower()- pasa a minusculas
#split() - separlo en partes(lista)
#join() - unir items usando separador
#find() - encontrar un sub-string
#replace() - reemplazar un 

#upper.
texto = "Este es el texto de Antonio";
resultado_mayusculas = texto.upper();
print(resultado_mayusculas)

#lower
print("***************")
resultado_minuscula = texto.lower();
print(resultado_minuscula);

#split
print("***************")
resultado_separdo = texto.split();
print(resultado_separdo)

#join
print("***************");
a = "Aprender";
b = "Python";
c = "es";
d = "genial";
e = " ".join([a,b,c,d]);
print(e);

#find
print("***************");
resultado_buscar = texto.find("el"); #nos dice la posicion de el
print(resultado_buscar);

#replace
print("***************");
resultado_remplazar = texto.replace("e","x"); #reemplaza e por x en el texto
print(resultado_remplazar);
