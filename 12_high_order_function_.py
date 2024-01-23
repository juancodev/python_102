# high order function con funcion

def increment(x): 
  return x + 1

def high_order_function(x, function):
  return x + function(x)

result = high_order_function(2, increment)
# 2 + (2 + 1)
print(result)

# high order function con lambda function

increment_lambda = lambda x: x + 1

high_order_function_lambda = lambda x, function: x + function(x)

result_2 = high_order_function_lambda(2, increment_lambda)
print(result_2)

result_3 = high_order_function_lambda(2, lambda x : x * 2)
print(result_3)
result_4 = high_order_function_lambda(2, lambda x : x + 5)
print(result_4)