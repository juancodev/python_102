import utils

data = [{
    'Country': 'Venezuela',
    'Population': 200
}, {
    'Country': 'Colombia',
    'Population': 300
}, {
    'Country': 'Mexico',
    'Population': 500
}, {
    'Country': 'Estados Unidos',
    'Population': 1000
}]

def run():
  keys, values = utils.get_population()
  
  print(keys, values)
  
  country = input("Ingresa el país => ")
  result_total = utils.get_population_by_country(data, country)
  
  print(result_total)

'''
Otro dato interesante es que pueden renombrar un módulo dentro del código para cuando lo usen usar una abreviación con as

import moduloconnombrelargo as m
'''

# Dualidad para poder ejecutar el script desde diferente archivo o en el mismo archivo

# Se le llama: Entry point

if __name__ == '__main__':
  run()