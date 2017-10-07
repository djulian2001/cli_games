# import random
from app.utilities import pop_list_by_position

class Player(object):

  def __init__(self,name,computer=False):
    self.name = name
    self.hand = []
    self.computer = computer
    # for poker, player might have a 'stack'

  def add_to_hand( self, list_of_objects ):
    """Add a list of objects (probably cards) to hand
      @list_of_objects as an interable 
    """
    for new_object in list_of_objects:
      self.hand.append( new_object )

  def remove_from_hand( self, position='top' ):
    """Remove an object from the player.hand and return that object
      @position as 'top' or ['random','bottom']
      returns: object pop'ed from hand
    """
    return pop_list_by_position( self.hand, position )
    