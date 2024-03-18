# Tener permiso de lectura y escritura
with open("files/text.txt", "r+") as file:
  for lines in file:
    print(lines)

  file.write('\n Esta es una nueva línea agregada desde write\n')

# r+ nos permite leer y escribir / w+ nos permite sobre-escribir
