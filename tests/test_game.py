import unittest
import copy
from random import shuffle

from app.game import Game
from app.game import Player


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
    g = Game(
      name='my_game',
      description="my cool game",
      players=['Tim','Pup'],
      total_players=2,
      max_team_size=1 )
    self.assertIsInstance( g, Game )
    self.assertIs( type( g.name ), str )
    # description
    self.assertIs( type( g.description ), str )
    # number of players
    # number of teams
    self.assertIs( type( g.total_players), int )
    self.assertIs( type( g.max_team_size ), int )
    self.assertIs( type( g.total_teams), int )
    self.assertEqual( g.total_teams, 2)
    self.assertEqual( len(g.players_out),0 )

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
    g = Game(
      name='adding',
      description='add players',
      players=['Teddy','Ruxin'] )

    self.assertIsInstance( g.players[0], Player )
    self.assertEqual( len(g.players), 2 )

  def test_game_method_exit_game(self):
    g = Game('help','help',['bob'])
    self.assertTrue( hasattr( g, "exit_game" ) )


if __name__=="__main__":
  unittest.main()
