import os
import random

def pop_list_by_position( list_object, position ):
  """From a list, pop a 'positional' object, and return that object'
    @position as 'top' or ['random','bottom']
    returns: pop'ed object from list
  """
  if position=='random':
    return list_object.pop( random.randrange( len( list_object ) ) )
  elif position=='bottom':
    return list_object.pop()
  return list_object.pop(0)

def clear_screen():
  dump = os.system('cls' if os.name=='nt' else 'clear')
