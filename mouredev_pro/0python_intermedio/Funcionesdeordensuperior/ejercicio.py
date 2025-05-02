from functools import reduce

# 1. Crea una función que reciba una función y un número, y devuelva el resultado de aplicar la función al número.


def apply_function(f, value):
    return f(value)


print(apply_function(lambda x: x + 3, 7))

# 2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.


def add_and_apply(a, b, f):
    return f(a + b)


print(add_and_apply(2, 3, lambda x: x * 2))

# 3. Crea una función que devuelva otra función que sume un número fijo.


def make_adder(fixed):
    return lambda x: x + fixed


add_five = make_adder(5)
print(add_five(10))


# 4. Usa map() con lambda para multiplicar cada número de una lista por 10.

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 10, numbers))
print(result)

# 5. Usa filter() con lambda para quedarte solo con los números pares.

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# 6. Usa reduce() con lambda para obtener la suma total de una lista.

numeros = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numeros)
print(total)

# 7. Escribe una funciÃ³n que devuelva una funciÃ³n que reciba un nombre y devuelva â€œHola, â€.


def greeting_function():
    return lambda name: "Hola Caracola, " + name


greet = greeting_function()
print(greet("Heredia"))

# 8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.


def count_matches(lst, condition):
    count = 0
    for item in lst:
        if condition(item):
            count += 1
    return count


print(count_matches([1, 5, 8, 3], lambda x: x > 4))

# 9. Crea una función que reciba dos funciones y un número, y las aplique en orden.


def apply_both(f1, f2, value):
    return f2(f1(value))


print(apply_both(lambda x: x + 2, lambda x: x * 3, 4))

# 10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).


def apply_to_list(lst, f):
    result = []
    for item in lst:
        result.append(f(item))
    return result


print(apply_to_list([1, 2, 3], lambda x: x * 2))