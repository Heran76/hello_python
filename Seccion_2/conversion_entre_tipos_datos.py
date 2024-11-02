#hacer casting transforma el dato
#implicita = python conveirte el tipo de datos en otro tipo de datos, automaticamente. En este proceso, el usuario no debe hacer nada.
#explicita = python necesita que el usaurio haga algo para convertir un tipo de dato a otro

#conversion implicita

num1 = 20;
num2 = 30.5;

num1 = num1 +num2 #comversion implita
print(num1);
print(type(num1));
print(num2);
print(type(num2));

#conversion explicita

num3 = 5.8;
num4 = int(num3);
print(num3);
print(type(num3));
print(num4) #la conversion quita todos los decimales.
print(type(num4));

print("*********************")

edad = input("Dime tu edad: ")
print(type(edad))

edad = int(edad)

print(type(edad))

nueva_edad = 1 + edad;
print(nueva_edad);