# funcion sin lambda


def increment(x):
  return x + 1


result = increment(10)
print(result)

# funcion con sintaxis lambda

increment_lambda = lambda x: x + 1

result_2 = increment_lambda(20)
print(result_2)

# varios parametros

full_name = lambda name, last_name: f'My full name is {name.title()} {last_name.title()}'

presentation = full_name('juan', 'montilla')

print(presentation)