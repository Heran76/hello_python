# 1. Declara y asigna valores a las siguientes variables:
# name: una cadena que contenga tu nombre.
# age: un nÃºmero entero que represente tu edad.
# height: un nÃºmero flotante que represente tu altura.
# Imprime cada variable en una lÃ­nea separada.

name = "Brais"
age = 37
height = 1.77

print(name)
print(age)
print(height)

# 2. Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuÃ¡ntos aÃ±os tienes.

print("Tengo " + str(age) + " años")

# 3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprí­mela.

is_student = True
print(is_student)

# 4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.

full_name = "Brais Moure"
print(len(full_name))

# 5. Declara tres variables en una sola lí­nea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.

name, surname, city = "Brais", "Moure", "Galicia"
print(name, surname, city)

# 6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en una variable color. Luego, imprime el valor ingresado.

color = input("Â¿Cuá es tu color favorito? ")
print(color)

# 7. Declara una variable fruit e inicí­zala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.

fruit = "Manzana"
print(fruit)
fruit = "Naranja"
print(fruit)

# 8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprí­melo.

price = 9.99
print(int(price))

# 9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.

address = "Calle 123, Ciudad"
address_len = len(address)
print(address_len)

# 10. Usa un tipo de dato forzado para declarar una variable phone, asegurádote de que siempre será¡ un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().

phone: int = 123456789
print(type(phone))
phone = 987654321
print(type(phone))