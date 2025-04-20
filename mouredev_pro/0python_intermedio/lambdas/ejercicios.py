# 1. Crea una lambda que sume dos números.

sum = lambda a, b: a + b
print(sum(3, 5))

# 2. Crea una lambda que calcule el cuadrado de un número.

square = lambda x: x ** 2
print(square(6))

# 3. Crea una lambda que devuelva el mayor de dos números.

greater = lambda a, b: a if a > b else b
print(greater(10, 25))

# 4. Crea una lambda que sume 10 a un número dado.

add_ten = lambda x: x + 10
print(add_ten(7))

# 5. Crea una lambda que devuelva el algoritmo caracter de una cadena.

last_char = lambda text: text[-1]
print(last_char("Python"))

# 6. Crea una lambda que indique si una palabra tiene más de 6 letras.

long_word = lambda word: len(word) > 6
print(long_word("Python"))
print(long_word("MoureDev"))

# 7. Crea una lambda que convierta una cadena a minúsculas.

to_lower = lambda text: text.lower()
print(to_lower("Â¡Hola, Python!"))

# 8. Crea una lambda que devuelva True si un número es positivo.

is_positive = lambda number: number > 0
print(is_positive(-1))
print(is_positive(8))

# 9. Crea una lambda que devuelva "Cadena vacía" si el string está vacio.

check_empty = lambda s: "Cadena vacÃ­a" if s == "" else "Cadena no vacÃ­a"
print(check_empty(""))
print(check_empty("Python"))

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.

price_with_tax = lambda price: price * 1.21
print(price_with_tax(100))