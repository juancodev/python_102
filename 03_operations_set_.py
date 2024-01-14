set_a = {'VE', 'CO', 'MX'}
set_b = {'MX', 'USA'}

'''
Union entre conjuntos, se necesita de un tercer resultante  Realiza la operacion “union”
'''

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# intercepción del conjunto: solamente se muestra quien los une

set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# diferentes del conjunto a menos el conjunto b

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# diferencia simétrica del conjunto: a y b pero sin la union de los dos

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)

# ejercicio

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = set()
# Escribe tu solución 👇

new_set = countries.union(northAm, centralAm, southAm)

print(new_set)

