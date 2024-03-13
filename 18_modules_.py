# importar modulos en Pyhton
# import para el sistema
import sys

road = sys.path
print(road)

# import para expresiones regulares
import re

text = 'Hola mundo soy Juan Montilla, tengo 25 años de edad y mi número de teléfono es 04149177752 y mi número de la suete es 3'

result = re.findall('[0-9]+', text)
print(result)

# import para tiempo en python

import time

timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

# import para collecciones de datos (dict)

import collections

numbers = [2, 1, 22, 11, 2, 35, 35, 2, 1, 11, 201]

counter = collections.Counter(numbers)

print(counter)