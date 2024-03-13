# crear modulos en Python


def get_population():
  keys = ['VE', 'COL', 'MEX', 'USA']
  values = [200, 500, 350, 1000]
  return keys, values


# modulo para validar si el dato existe en el pais
def get_population_by_country(data: list, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result
