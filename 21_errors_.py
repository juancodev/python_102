# Utilizando la sentencia try - except
print('Inicio de la ejecución del programa')

try:
  print(0 / 0)
except ZeroDivisionError as err:
  print(err)

try:
  def sum(x,y):
   return x + (y * 2) 
  result = sum(2, 2)
  assert result == 4, 'El resultado debe ser 4'
except AssertionError as error:
  print(error)

try:
  age = 15
  if age < 18:
    raise Exception('You are younger')
except Exception as err:
  print(err)

print('Fin de la ejecución del programa')
