items = [
  {
    "clothe": "shirt",
    "price": 200
  },
  {
    "clothe": "pants",
    "price": 100
  },
  {
    "clothe": "dress",
    "price": 300
  }
]

result = list(map(lambda element: element['price'], items))
print(result)

def add_taxes(item):
  items_copy = item.copy()
  print(items_copy)
  items_copy["taxes"] = items_copy["price"] * .16
  return items_copy

total_items = list(map(add_taxes, items))
print(total_items)