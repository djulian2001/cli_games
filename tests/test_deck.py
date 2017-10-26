import unittest

from tests.seeds_testing import Seeds_Decks
from app.deck import Deck
from app.card import Card

class Test_Deck( unittest.TestCase, Seeds_Decks ):

  # Unittest general 
  def setUp(self):
    """If there was required actions to set the running enviornment for the app"""
    pass
  def tearDown(self):
    """If there was a required clean up."""
    pass

  def test_deck_interface(self):
    d = self.seed_deck()
    self.assertIsInstance( d , Deck )
    self.assertIs( type( d.unique_cards), bool )
    self.assertIs( type( d.cards), list )
    self.assertIs( type( d.deck_rules ), dict )
    self.assertIs( type( d.deck_rules['suit_rules'] ), list )
    self.assertIs( type( d.deck_rules['suit_rules'][0] ), tuple )
    self.assertIs( type( d.deck_rules['card_rules'] ), list )
    self.assertIs( type( d.deck_rules['card_rules'][0] ), tuple )

  def test_deck_shuffle(self):    
    d1 = self.seed_deck()
    self.assertNotEqual( d1.cards, d1.shuffled() )
    # Might need to expand this?

  def test_deck_interface_build_deck(self):
    d = self.seed_deck()
    self.assertIs( type( d.get_cards() ), list )
    for i in d.cards:
      self.assertIsInstance( i, Card )
