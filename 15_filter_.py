numbers = [1, 2, 3, 4, 5, 6]
# filter funciona siempre y cuando se haya cumplido su condición
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
# inmutablilidad
print(numbers)