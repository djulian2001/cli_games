
class Card(object):
  """
    A card object has variable number of attributes, depending on the type of deck,
      attributes might look like label, rank, suit, color, symbols, etc...
  """
  def __init__(self,label,rank,suit,suit_rank):
    self._label = label
    self._rank = rank
    self._suit = suit
    self._suit_rank = suit_rank

  def __str__(self):
    """Pretty Print the objects"""
    return "{l} of {s}".format( l=self.label.capitalize(), s=self.suit.capitalize() )

  @property
  def label(self):
    return self._label

  @property
  def rank(self):
    return self._rank

  @property
  def suit(self):
    return self._suit

  @property
  def suit_rank(self):
    return self._suit_rank

