# Leer archivos desde Python

file = open("files/text.txt")

#print(file.read())

# pero también hay otra forma para leer línea por línea y es con readline

print(file.readline())
print(file.readline())
print(file.readline())

# pero la mejor forma de aprovechar los recurso de la memoria de python seria abrilo con with

with open("files/text.txt") as files:
  for line in files:
    print(line)

# siempre que se abra el archivo, debe ser cerrado para evitar consumir la memoria ram.

file.close()