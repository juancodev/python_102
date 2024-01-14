set_contries = {'ven', 'col', 'mex', 'usa'}

# tamaño de un conjunto
size = len(set_contries)
print(size)

# saber si hay o no hay elementos en un conjunto
print('ven' in set_contries)
print('pr' in set_contries)

# adicionar un conjunto
set_contries.add('arg')
print(set_contries)

set_contries.add('uru')
print(set_contries)

# actualizar un conjunto, lo que hace es unirlo al conjunto existente.
set_contries.update({'par', 'cub'})
print(set_contries)
'''
set_contries.update('can', 'rus')
print(set_contries)
'''

# remover un conjunto existente; de no existir se crashea la app
set_contries.remove('par')
print(set_contries)

# descartar el error me sirve para evitar el crasheo de mi app
set_contries.discard('pr')
print(set_contries)

# limpiar un conjunto y dejarlo en vacío
set_contries.clear()
print(len(set_contries))
