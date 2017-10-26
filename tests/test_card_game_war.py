import unittest

from tests.seeds_testing import Seeds_Card_Game_War

from app.card import Card
from app.player import Player

class Test_Card_Game_War( unittest.TestCase, Seeds_Card_Game_War ):
  """Unit tests for the class Card_Game_War"""
    
  def test_card_game_war_interface( self ):
    """The war card game"""
    w2_players=['alex','dave']
    w1 = self.seed_a_card_game_of_war()
    w2 = self.seed_a_card_game_of_war( player_list=w2_players )
    self.assertEqual( w1.name, w2.name )
    self.assertEqual( w1.description, w2.description )
    self.assertEqual( w1.total_players, w2.total_players )
    self.assertEqual( w1.max_team_size, w2.max_team_size )
    self.assertEqual( w1.rules, w2.rules )
    self.assertNotEqual( w1.players, w2.players )
    for player in w2.players:
      self.assertTrue( player.name in w2_players )

  def test_war_method_deal_cards(self):
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    self.assertEqual( 26, len( w1.get_player_by_name('pete').hand ) )
    self.assertEqual( 26, len( w1.get_player_by_name('alex').hand ) )

  def test_war_method_turn(self):
    """
        which triggers a card turn() requests player input of turn options [flip], 
          a turn option configures a turn event which pops the cards into the pot
          then compares cards ranks ->
            this could result in a war condition or a take_pot for a player with the highest rank
    """
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    self.assertTrue( hasattr( w1, "turn") )
    output = w1.turn( player=w1.players[0], choice=1 )
    self.assertIs( type( output ), tuple )
    self.assertIs( type( output[0] ), int )
    self.assertIs( type( output[1] ), str )
    self.assertEqual( len( w1.pot ), 1)
    self.assertEqual( len(w1.players[0].hand), 25 )
    self.assertIs( type( w1.pot[0] ), Card )
    with self.assertRaises( TypeError ):
      output2 = w1.turn(player=w1.players[1], choice=None)
    with self.assertRaises( SystemExit ) as cm:
        w1.turn( w1.players[0], choice=9 )
    self.assertEqual( cm.exception.code, 1 )

  def test_war_method_compare_cards_normal(self):
    w1 = self.seed_a_card_game_of_war()
    self.assertTrue( hasattr( w1 , 'compare_cards' ) )
    w1.deal_cards()
    aturn=[]
    for player in w1.players:
      aturn.append( ( player, w1.turn( player,choice=1 ) ) )
    self.assertEqual( len( aturn ), 2 )
    output = w1.compare_cards( aturn )
    if output == None:
      self.assertTrue( aturn[0][1] != aturn[1][1] )
    else:
      self.assertIs( type(output), Player )

  def test_war_method_compare_cards_player_one_wins(self):
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    aturn= [  ( w1.players[0], (1,'player one') ),
              ( w1.players[1], (3,'player two') ), ]
    player_one = w1.compare_cards( aturn )
    self.assertEqual( player_one, w1.players[0] )

  def test_war_method_compare_cards_none(self):
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    aturn= [  ( w1.players[0], (1,'player one') ),
              ( w1.players[1], (1,'player one') ), ]
    player_none = w1.compare_cards( aturn )
    self.assertIsNone( player_none )

  def test_war_method_it_is_war(self):
    w1 = self.seed_a_card_game_of_war()
    self.assertTrue( hasattr( w1, 'it_is_war' ) )
    w1.deal_cards()
    # player doesn't have the cards to play, they lose!
    w1.it_is_war( cards = 3 )
    self.assertEqual( len( w1.players[0].hand ), 23 )
    self.assertEqual( len( w1.players[1].hand ), 23 )

  def test_war_method_it_is_war_out_of_cards(self):
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    for i in range(24):
      w1.players[1].hand.append( w1.players[0].remove_from_hand('top') )
    self.assertEqual( len( w1.players[0].hand ),2 )
    self.assertFalse( w1.check_player_is_out( w1.players[0] ) )

  def test_war_method_who_won(self):
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    self.assertTrue( hasattr( w1, 'who_won' ) )
    for i in range(26):
      w1.players[1].hand.append( w1.players[0].remove_from_hand('top') )
    player = w1.who_won()      
    self.assertIsInstance( player, Player )
    self.assertEqual( len( player.hand ), 52 )

  def test_war_method_win(self):
    w1 = self.seed_a_card_game_of_war()
    self.assertTrue( w1.win() )
    w1.deal_cards()
    self.assertFalse( w1.win() )
    w1.players[0].hand = []
    self.assertEqual( len( w1.players[0].hand ), 0 )
    self.assertTrue( w1.win() )

  def test_war_method_status(self):
    w1 = self.seed_a_card_game_of_war()
    self.assertTrue( hasattr( w1, 'status' ) )

  def test_war_method_turn_choices(self):
    w1 = self.seed_a_card_game_of_war()
    w1.deal_cards()
    self.assertTrue( hasattr( w1, 'turn_choice' ) )
