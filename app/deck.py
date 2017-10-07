from app.card import Card
from random import shuffle

class Deck(object):
  """
    A Deck is made up of a set of card objects.
  """
  # def __init__(self, total_cards, unique_cards, deck_rules):
  def __init__(self, unique_cards, deck_rules):
    self.unique_cards = unique_cards
    self.deck_rules = deck_rules
    self.cards = self.get_cards()

  # def __str__(self):
  #   return "Deck: {d}".format( d=self.cards )

  def shuffled(self):
    return shuffle( self.cards )

  def get_cards(self):
    cards = []
    def add_card():
      cards.append( Card(
        label=card_rule[1],
        rank=card_rule[0],
        suit=suit_rule[1],
        suit_rank=suit_rule[2] ) )
    
    for suit_rule in self.deck_rules['suit_rules']:
      for card_rule in self.deck_rules['card_rules']:
        if self.unique_cards:
          add_card()
        else:
          for card_count in range(card_rule[2]):
            add_card()
    
    return cards
