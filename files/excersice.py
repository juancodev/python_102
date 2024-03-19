import csv
import functools

def read_csv(path):
  with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list()
    for row in reader:
      data.append(int(row[1]))
      total = functools.reduce(lambda acc, val: acc + val, data)
    return total

response = read_csv('./files/data.csv')
print(response)