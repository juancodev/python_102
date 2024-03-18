# errores comunes y manejadores de errores en Python

# print(0/0)) => SyntaxError
# print(0/0) => ZeroDivisionError
# print(result) => NameError

# Podemos hacer 'tipos de errores que queremos recibir'

sum = lambda x, y: x + y
assert sum(2,2) == 4

# Errores con excepciones

age = 15
if age < 18:
  raise Exception('You are younger')