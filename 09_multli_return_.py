# Poder definir multiples parámetros
print('----------Multi params with only return------------')


def print_volumen(width, length, depth):
  return width * length * depth


result = print_volumen(10, 20, 3)

print(result)

# retornar valores por defecto, ya que si no se mandan parámetros se genera un error.
# retornamos un valor
print('----------default values with only return------------')


def calculate_volum(width=1, length=1, depth=1):
  return width * length * depth


result1 = calculate_volum()

print(result1)

# Pasar un solo parametro
print('----------one param with only return------------')


def calculate_volum2(width=1, length=1, depth=1):
  return width * length * depth


result2 = calculate_volum2(length=20)
print(result2)

# retornar múltiples valores
print('----------Multi return------------')


def calculate_volum1(width=1, length=1, depth=3):
  return width * length * depth, width**2, 'Calculated'


result_total = calculate_volum1(10, 20, 3)
print(result_total)

# Guardar retorno por separado
print('----------Save return for part------------')


def calculate_volum3(width=1, length=1, depth=3):
  return width * length * depth, width**2, 'Calculated'


result_total = calculate_volum3(10, 20, 3)
print(f'Position 0: {result_total[0]}')
print(f'Position 1: {result_total[1]}')
print(f'Position 2: {result_total[2]}')
