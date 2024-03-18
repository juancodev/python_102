# los iterable son un tipo de objecto que nos sirve para hacer iteraciones de forma más controlada

# De esta manera no se puede controlar el iterador, ya que el ciclo for lo recorre automático

for i in range(1, 11):
  print(i)

# Para poder controlar esto, se necesita del método iter()

iterable = iter(range(1, 4))
print(iterable)

# output => <range_iterator object at 0x7bbd0bc9e580>

#para mostrar valor por valor, se necesita del método next()

print(next(iterable))
print(next(iterable))
print(next(iterable))

# cuando ya no puede iterar más, lanzará un error de exepción
