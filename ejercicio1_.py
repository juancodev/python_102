'''
Si recibes una computadora, debes retornar el mensaje: "Con mi computadora puedo programar usando Python".
Si recibes un celular, debes retornar el mensaje: "En mi celular puedo aprender usando la app de Platzi".
Si recibes un cable, debes retornar el mensaje: "¡Hay un cable en mi bota!".
Y si no recibes ninguno de estos valores, debes retornar el mensaje: "Artículo no encontrado".
'''


def message_creator(text):
  # Escribe tu solución 👇
  text = text.lower()
  if text == 'computadora':
    return 'Con mi computadora puedo programar usando Python'
  elif text == 'celular':
    return 'En mi celular puedo aprender usando la app de Platzi'
  elif text == 'cable':
    return '¡Hay un cable en mi bota!'
  else:
    return 'Artículo no encontrado'


text = 'computadora'
response = message_creator(text)
print(response)
