numbers = []
for element in range(1, 11):
  numbers.append(element)

print(numbers)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = []
for element in range(1, 11):
  numbers.append(element * 2)

print(numbers)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# list comprehension
numbers_v2 = [element2 for element2 in range(1, 11)]
print(numbers_v2)

numbers_double = [element2 * 2 for element2 in range(1, 11)]
print(numbers_double)

# condicional

numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)

print(numbers)

# condicional con list comprehension

numbers_condition = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_condition)
'''
Las comprehensions de Python son una forma concisa y legible de crear listas, conjuntos y diccionarios en una sola línea de código. La sintaxis básica de las comprehensions es la siguiente:

Lista comprehension: [expresión for elemento in iterable] Conjunto comprehension: {expresión for elemento in iterable} Diccionario comprehension: {clave: valor for elemento in iterable}
'''
