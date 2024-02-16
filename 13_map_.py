numbers = [1, 2, 3, 4]

# map es una funcion que me permite devolver un cambio de valores

numbers_v2 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)

# map nos permite iterar diferentes matrices

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)

#Sintaxis.
# map(function, iterables)