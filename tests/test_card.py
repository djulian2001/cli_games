import unittest

from app.card import Card

class Test_Card( unittest.TestCase ):
  """Testing of the class card"""

  def test_card_interface(self):
    """once the card is instantiated should not change cards values"""
    c = Card(label='test',rank=99,suit='nice',suit_rank=1)
    self.assertIsInstance( c, Card)
    # card characteristics
    self.assertIs( type( c.label ), str )
    self.assertIs( type( c.rank ), int )
    self.assertIs( type( c.suit), str )
    self.assertNotEqual( c.label, 'no thanks')
    self.assertEqual( c.label, 'test')
    self.assertNotEqual( c.rank, 100 )
    self.assertEqual( c.rank, 99 )
    # this does not apply to this game...
    self.assertIs( type( c.suit_rank), int )
    self.assertEqual( c.suit_rank, 1 )
    self.assertNotEqual( c.suit_rank, 2 )
    with self.assertRaises( AttributeError ):
      c.rank = 89
    with self.assertRaises( AttributeError ):
      c.label = "no this value"
