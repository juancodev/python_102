dict = {}
for i in range(1, 6):
  dict[i] = i * 2

print(dict)

# dict comprehension

dict_v2 = {i: i * 2 for i in range(1, 6)}
print(dict_v2)

# other case with countries
import random

countries = ['MEX', 'COL', 'VEN', 'PER', 'BRA']
population = {}

for country in countries:
  population[country] = random.randint(1, 100)

print(population)

# dict comprehension

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

# multi list

names = ['Juan', 'Cynthia', 'Maria']
ages = [25, 24, 56]

# para unir listas distintas en una sola, utilizamos el método zip de python

# print(zip(names, ages)) - esto así me devuelve una referencia

print(list(zip(names, ages)))

person = {name : age for (name, age) in zip(names, ages)}
print(person)

