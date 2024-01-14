# codigo sin reutilizar
sum = 0
for x in range(1, 10):
  sum += x

print(sum)

# codigo optimizado con function
print('----------without return---------------')
def sumValues(min, max):
  sumTotal = 0
  for x in range(min, max):
    sumTotal += x
  print(sumTotal)
  
sumValues(1, 11)
sumValues(1, 100)
sumValues(20, 30)

# retornar valores
print('----------with return---------------')
def sum_with_return(min, max):
  sum = 0
  for x in range(min, max):
    sum += x
  return sum

result1 = sum_with_return(2, 12)
result2 = sum_with_return(3, 13)
result3 = sum_with_return(4, 20)

print(result1, result2, result3)