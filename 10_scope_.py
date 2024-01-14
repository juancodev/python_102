# scope = ámbito
global_scope = 'Soy una variable global'

# contexto o ámbito local
def function_local_scope():
  # Esta variable con el mismo nombre del ámbito global != a la variable del ámbito global.
  global_scope = 'Nuevo valor'
  
  local_scope = 'Soy una variable local'

  local_scope += '. Solamente puedo ser utilizada en este scope'

  return local_scope


print(global_scope)
local_value = function_local_scope()
print(local_value)