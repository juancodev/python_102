import random

countries = ['MEX', 'COL', 'VEN', 'BRA', 'USA']

population_v1 = {country : random.randint(1, 100) for country in countries}

print(population_v1);

population_with_condiction = {country : population for (country, population) in population_v1.items() if population > 20}

print(population_with_condiction)

# dict comprehension con condicional en texto

text = 'Hello world! I am a Frontend Developer'

unique = { character : text.count(character) for character in text if character in 'aeiou'}
print(unique)

test1 = {}
test2 = ()
test3 = set()

print(type(test1), type(test2), type(test3))