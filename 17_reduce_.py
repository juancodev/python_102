# Las nuevas versiones de Python ya trae reduce incluido
# pero para evitar problema se importa las functools
import functools

numbers = [1, 2, 3, 4]

#lambda function
result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)


# def
def accum(counter, item):
  print('counter => ', counter)
  print('item => ', item)
  return counter + item


accumulation = functools.reduce(accum, numbers, 0)

print(accumulation)
