import unittest

from tests.test_game import Test_Game
from tests.test_card_game import Test_Card_Game
from tests.test_card_game_war import Test_Card_Game_War
from tests.test_player import Test_Player
from tests.test_deck import Test_Deck
from tests.test_card import Test_Card

def suite():
  run_tests = [ 
    Test_Game, 
    Test_Card_Game,
    Test_Player,
    Test_Deck,
    Test_Card,
    Test_Card_Game_War,  ]
  suite = unittest.TestSuite()

  for run_test in run_tests:
    suite.addTest( unittest.makeSuite( run_test ) )

  return suite

if __name__ == '__main__':
  runner = unittest.TextTestRunner() 
  runner.run ( suite() )