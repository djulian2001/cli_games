import unittest
import copy
from random import shuffle

from tests.seeds_testing import Seeds_Players

from app.player import Player
from app.card import Card

# class Test_Unittest(unittest.TestCase, Seeds_Card_Game):
class Test_Player( unittest.TestCase, Seeds_Players ):
  
  # Unittest general 
  def setUp(self):
    """If there was required actions to set the running enviornment for the app"""
    pass
  def tearDown(self):
    """If there was a required clean up."""
    pass

  def test_player_interface(self):
    p = self.seed_player()
    self.assertTrue( p.computer )
    self.assertIsInstance( p, Player )
    self.assertIs( type(p.hand), list )

  def test_player_method_add_list_of_objects_to_hand_default(self):
    p = self.seed_player(name="Bear")
    obj1 = [1,2,3]
    obj2 = Card(label='test1',rank=99,suit='nice',suit_rank=1)
    obj3 = Card(label='test2',rank=1,suit='nice',suit_rank=1)
    obj4 = 'a coin'

    l = [obj4,obj3,obj2,obj1]
    
    self.assertFalse( obj1 in p.hand )
    self.assertEqual( len(p.hand),0 )
    p.add_to_hand(l)
    self.assertTrue( obj1 in p.hand )
    self.assertEqual(len(l),len(p.hand))
    self.assertEqual( len(p.hand),4 )
    self.assertNotEqual( obj3, p.hand[3] )
    self.assertEqual( obj3, p.hand[1] )
    self.assertEqual( obj4, p.hand[0] )
    with self.assertRaises(TypeError):
      p.add_to_hand(obj3)

  def test_player_method_remove_object_from_hand_default(self):
    p = self.seed_player(name="Teddy Bear")
    obj1 = [1,2,3]
    obj2 = Card(label='test1',rank=99,suit='nice',suit_rank=1)
    obj3 = Card(label='test2',rank=1,suit='nice',suit_rank=1)
    obj4 = 'a coin'
    l = [obj4,obj3,obj2,obj1]
    p.add_to_hand(l)
    postion='top'
    self.assertEqual( p.remove_from_hand(postion), obj4 )

  def test_player_remove_object_from_hand_bottom(self):
    p = self.seed_player(name="Teddy Bear")
    obj1 = [1,2,3]
    obj2 = Card(label='test1',rank=99,suit='nice',suit_rank=1)
    obj3 = Card(label='test2',rank=1,suit='nice',suit_rank=1)
    obj4 = 'a coin'
    l = [obj4,obj3,obj2,obj1]
    p.add_to_hand(l)
    postion='bottom'
    self.assertEqual( p.remove_from_hand(postion), obj1 )

  def test_player_method_remove_object_from_hand_random(self):
    p = self.seed_player(name="Teddy Bear")
    obj1 = [1,2,3]
    obj2 = Card(label='test1',rank=99,suit='nice',suit_rank=1)
    obj3 = Card(label='test2',rank=1,suit='nice',suit_rank=1)
    obj4 = 'a coin'
    l = [obj4,obj3,obj2,obj1]
    p.add_to_hand(l)
    p.remove_from_hand('top')
    p.remove_from_hand('bottom')
    postion='random'
    self.assertNotEqual( p.remove_from_hand(postion), obj1 )
    self.assertNotEqual( p.remove_from_hand(postion), obj4 )
    self.assertFalse( obj1 in p.hand )
