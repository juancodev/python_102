# forma de crear conjuntos en Python
set_contries = {'ven', 'col', 'mex', 'usa'}
print(set_contries)
print(type(set_contries))

# el conjunto no acepta valores repetidos, no tiene un orden de jerarquia

set_numbers = {1, 2, 3, 25, 3, 15}
print(set_numbers)

set_types = {True, 2, 1.1, False, 'str'}
print(set_types)

# crear o partir desde un valor de string
string_values = set('Hello')
print(string_values)

# crear o partir desde numeros
set_from_tuples = set((2, 3, 4, 5, 6, 6, 7, 8))
print(set_from_tuples)

# crear o partir desde una lista
list_numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9,10]
set_from_list = set(list_numbers)
print(set_from_list)

# Esto nos sirve para evaluar un caso de tener una lista repetida y eliminar los valores repetidos.

print(list(set_from_list))