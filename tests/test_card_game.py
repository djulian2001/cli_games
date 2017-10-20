import unittest
import copy
from random import shuffle

from tests.seeds_testing import Seeds_Card_Game
from app.card_game import Card_Game
from app.game import Game
from app.player import Player
from app.card import Card
from app.deck import Deck

class Test_Card_Game(unittest.TestCase, Seeds_Card_Game):
  """Card_Game test suite for the card game class""" 
  def setUp(self):
    """If there was required actions to set the running enviornment for the app"""
    pass

  def tearDown(self):
    """If there was a required clean up."""
    pass

  def test_card_game_interface(self):
    self.assertTrue( issubclass( Card_Game, Game ) )
    cg = Card_Game(
      name="a_game",
      description="having fun with friends",
      card_game_rules={'stuff':'yo'},
      players=['Jack','Sara'])
    g = Game(
      name="a_game",
      description="having fun with friends",
      players=[])
    self.assertIsInstance( cg, Card_Game )
    self.assertEqual( cg.total_teams, g.total_teams )
    self.assertIs( type( cg.decks ), dict )
    self.assertIsNone( cg.decks['main'] )
    self.assertIs( type(cg.card_game_rules), dict )
    self.assertIs( type(cg.players), list )
    self.assertIsInstance( cg.pot, list )
    self.assertIsInstance( cg.players[0], Player )
    self.assertEqual( len( cg.players), 2 )

  def test_card_game_method_add_to_pot(self):
    cg = self.seed_a_card_game()  
    card_count = len(cg.decks['main'].cards)
    for i in range( card_count ):
      cg.pot.append( cg.decks['main'].cards.pop(0) )

    self.assertEqual(len(cg.pot),card_count)

  def test_card_game_method_take_pot(self):
    cg = self.seed_a_card_game()
    for i in range(len(cg.decks['main'].cards)-3):
      cg.pot.append( cg.decks['main'].cards.pop() )
    player = cg.get_player_by_name('Ruxin')
    cg.player_takes_pot( player )
    pot_cards = copy.deepcopy( cg.pot )
    self.assertEqual( len(cg.pot),0 )
    self.assertEqual( len( cg.get_player_by_name('Ruxin').hand ), 3 )
    for card in pot_cards:
      self.assertTrue( card in cg.get_player_by_name('Ruxin').hand )

  def test_card_game_method_get_player_by_name(self):
    cg = self.seed_a_card_game()
    player = cg.get_player_by_name('Ruxin')
    self.assertIsInstance( player, Player )
    self.assertIsNone( cg.get_player_by_name('Alf') )

  def test_card_game_method_show_game_status(self):
    cg = self.seed_a_default_dealt_card_game()
    # generate game state output
    output = cg.get_game_state()
    self.assertIs( type(output), str )

    for player in cg.players:
      self.assertTrue( player.name in output )

  def test_card_game_method_get_card_from_deck(self):
    cg = self.seed_a_card_game()
    name_of_deck = 'main'
    orig_deck_count = len( cg.decks[name_of_deck].cards )
    a_card = cg.get_card_from_deck( name_of_deck )
    self.assertIsInstance( a_card, Card )
    self.assertEqual( orig_deck_count-1, len( cg.decks[name_of_deck].cards ) )

  def test_card_game_method_get_decks(self):
    cg = self.seed_a_card_game_poker_deck()
    self.assertIsNotNone( cg.decks["main"] )
    self.assertIsInstance( cg.decks['main'], Deck )
    self.assertEqual( len( cg.decks['main'].cards), 52 )

  def test_card_game_method_deal_cards_default(self):
    cg = self.seed_a_card_game()
    cards_dealt_each_player = 2
    cards_dealt_each_rotation = 1
    deal_from_deck='main'
    cg.deal_cards( 
      cards_per_player=cards_dealt_each_player,
      per_loop=cards_dealt_each_rotation,
      deck=deal_from_deck,
      position="top" )

    for player in cg.players:
      self.assertEqual( len(player.hand),2 )
    self.assertEqual( len(cg.decks['main'].cards),2 )

  def test_card_game_method_deal_cards_with_remainder(self):

    cg = copy.deepcopy( self.seed_a_card_game() )
    cards_dealt_each_player = 3
    cards_dealt_each_rotation = 2
    deal_from_deck='main'
    cg.deal_cards( 
      cards_per_player=cards_dealt_each_player,
      per_loop=cards_dealt_each_rotation,
      deck=deal_from_deck,
      position="random" )
    for player in cg.players:
      self.assertEqual( len(player.hand),3 )
    self.assertEqual( len(cg.decks['main'].cards),0 )

  def test_card_game_method_win_conditions(self):
    wg = self.seed_a_card_game()
    self.assertTrue( hasattr(wg,'check_win_condition'))
    # EXPAND THIS

if __name__ == '__main__':
  unittest.main()