import unittest
import copy
from random import shuffle

from app.game import Game
from app.player import Player


class Test_Game(unittest.TestCase):
# class Test_Unittest(unittest.TestCase):
  
  # Unittest general 
  def setUp(self):
    """If there was required actions to set the running enviornment for the app"""
    pass
  def tearDown(self):
    """If there was a required clean up."""
    pass
  
  def test_game_interface(self):
    p1 = Player('Tim')
    p2 = Player('Pup')
    g = Game(
      name='my_game',
      description="my cool game",
      players=[p1,p2],
      total_players=2,
      max_team_size=1 )
    self.assertIsInstance( g, Game )
    self.assertIs( type( g.name ), str )
    self.assertIs( type( g.description ), str )
    self.assertIs( type( g.total_players), int )
    self.assertIs( type( g.max_team_size ), int )
    self.assertIs( type( g.total_teams), int )
    self.assertEqual( g.total_teams, 2)
    self.assertEqual( len(g.players_out),0 )

  def test_game_attribute_players(self):
    with self.assertRaises( AssertionError ):
      Game( name='should fail', description = 'really fail', players = None )
    with self.assertRaises( AssertionError ):
      Game( name='should fail', description = 'really fail', players = (None,None) )

  def test_game_method_player_is_out(self):
    g = Game(
      name='adding',
      description='add players',
      players=['Teddy','Ruxin'] )

    player = g.players[0]
    g.player_is_out( player )
    self.assertEqual( len( g.players ), 1 )
    self.assertEqual( len( g.players_out ), 1 )

  def test_game_method_set_players(self):
    p1 = Player('Teddy')
    p2 = Player('Ruxin')
    g = Game(
      name='adding',
      description='add players',
      players=[p1,p2] )

    self.assertIsInstance( g.players[0], Player )
    self.assertEqual( len(g.players), 2 )

  def test_game_method_exit_game(self):
    g = Game('help','help',['bob'])
    self.assertTrue( hasattr( g, "exit_game" ) )
