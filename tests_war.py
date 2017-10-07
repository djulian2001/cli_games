import unittest
import copy
from random import shuffle

from app.game import Game
from app.card_game import Card_Game
from app.deck import Deck
from app.card import Card
from app.player import Player

class Test_Unittest(unittest.TestCase):
  
  # Unittest general 
  def setUp(self):
    """If there was required actions to set the running enviornment for the app"""
    pass
  def tearDown(self):
    """If there was a required clean up."""
    pass
  def test_assert(self):
    assert True
  def test_assertFalse(self):
    self.assertFalse(False)

  # SEEDING for REUSE:
  def seed_a_card_game(self):
    cg_card_game_rules ={
      "game_rules":[(1,"rule 1",5)],
      "deck_rules":{
        "main":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1)] 
        }, }, }

    return Card_Game(
      name='adding',
      description='add players',
      players=['Teddy','Ruxin'],
      card_game_rules=cg_card_game_rules )

  # APPLICATION TESTS:
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

  def test_game_set_players(self):
    g = Game(
      name='adding',
      description='add players',
      players=['Teddy','Ruxin'] )

    self.assertIsInstance( g.players[0], Player )
    self.assertEqual( len(g.players), 2 )

    cg_card_game_rules ={
      "game_rules":[(1,"rule 1",5)],
      "deck_rules":{
        "main":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1)] 
        }, }, }

    cg = Card_Game(
      name='adding',
      description='add players',
      players=['Teddy','Ruxin'],
      card_game_rules=cg_card_game_rules )

    self.assertIsInstance( cg.players[0], Player )
    self.assertEqual( len( cg.players), 2 )

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

  def test_card_game_add_to_pot(self):
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
    cg = self.seed_a_card_game()

  def test_card_game_method_get_card_from_deck(self):
    cg = self.seed_a_card_game()
    name_of_deck = 'main'
    orig_deck_count = len( cg.decks[name_of_deck].cards )
    a_card = cg.get_card_from_deck( name_of_deck )

    self.assertIsInstance( a_card, Card )
    self.assertEqual( orig_deck_count-1, len( cg.decks[name_of_deck].cards ) )

  def test_card_game_method_get_decks(self):
    cg_name = 'game'
    cg_description = 'game desc'
    cg_card_game_rules ={
      "game_rules":[(1,"rule 1",5),(2,"rule 2",5),(2,"subrule 2.1",6)],
      "deck_rules":{
        "main":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red"),(3,"diamonds","red"),(4,"clubs","black")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1),(4,"jack",1),(5,"ten",1),(6,"nine",1),(7,"eight",1),(8,"seven",1),(9,"six",1),(10,"five",1),(11,"four",1),(12,"three",1),(13,"two",1)] 
        },
        "other":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red"),(3,"diamonds","red"),(4,"clubs","black")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1),(4,"jack",1),(5,"ten",1),(6,"nine",1),(7,"eight",1),(8,"seven",1),(9,"six",1),(10,"five",1),(11,"four",1),(12,"three",1),(13,"two",1)] 
        }, }, }

    cg = Card_Game(
      name=cg_name,
      description=cg_description,
      players=["max","brit","Rosco"],
      card_game_rules=cg_card_game_rules )

    self.assertIsNotNone( cg.decks["main"] )
    self.assertIsInstance( cg.decks['main'], Deck )
    self.assertEqual( len( cg.decks['main'].cards), 52 )
    # for card in cg.decks['main'].cards:
    #   print(card)

# rule configuration injection? or build into interfaces? or both?
  def test_card_game_method_deal_cards(self):
    """
      deal cards to players:
        cards get delt from the deck, one at a time to each player
        to each players hand, 
        takes an int
        a game can have many dealt cards, not all players are dealt cards
    """
    cg = self.seed_a_card_game()
    cards_dealt_each_player= 2

    


  def test_card_game_win_conditions(self):
    # from app import 
    # determine win
    pass

  def test_player_interface(self):
    p_name = "Teddy"
    p = Player(
      name=p_name,
      computer=True )

    self.assertTrue( p.computer )
    self.assertIsInstance( p, Player )
    self.assertIs( type(p.hand), list )

  def test_player_add_list_of_objects_to_hand(self):
    p_name="Bear"
    p = Player( name=p_name )
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

  def test_player_remove_object_from_hand(self):
    p_name = "Teddy Bear"
    p = Player(name=p_name)
    obj1 = [1,2,3]
    obj2 = Card(label='test1',rank=99,suit='nice',suit_rank=1)
    obj3 = Card(label='test2',rank=1,suit='nice',suit_rank=1)
    obj4 = 'a coin'
    l = [obj4,obj3,obj2,obj1]
    p.add_to_hand(l)
    postion='top'
    self.assertEqual( p.remove_from_hand(postion), obj4 )
    postion='bottom'
    self.assertEqual( p.remove_from_hand(postion), obj1 )
    postion='random'
    self.assertNotEqual( p.remove_from_hand(postion), obj1 )
    self.assertNotEqual( p.remove_from_hand(postion), obj4 )
    self.assertFalse( obj1 in p.hand )

# manage players war.py
  # turns (set up rules)
  # cards (set by deck rules)

# keep track of games state of cards
  # cards in play just flipped
  # cards in pot on table
  # cards in hand by players
  # cards in deck

  def test_deck_interface(self):
    rules = {
      "suit_rules":[
        (1,"bar","red"),(2,"fuz","blue"),(2,"dez","pink"), ],
      "card_rules":[
        (1,"fish",1),(2,"dog",1),(3,"cat",2),]
      }

    d = Deck(
        unique_cards=False,
        deck_rules=rules)
    self.assertIsInstance( d , Deck )
    self.assertIs( type( d.unique_cards), bool )
    self.assertIs( type( d.cards), list )
    self.assertIs( type( d.deck_rules ), dict )
    self.assertIs( type( d.deck_rules['suit_rules'] ), list )
    self.assertIs( type( d.deck_rules['suit_rules'][0] ), tuple )
    self.assertIs( type( d.deck_rules['card_rules'] ), list )
    self.assertIs( type( d.deck_rules['card_rules'][0] ), tuple )

  def test_deck_shuffle(self):
    rules = {
      "suit_rules":[
        (1,"bar","red"),(2,"fuz","blue"),(2,"dez","pink"), ],
      "card_rules":[
        (1,"fish",1),(2,"dog",1),(3,"cat",2),] }
    
    d1 = Deck(
        unique_cards=False,
        deck_rules=rules )

    self.assertNotEqual( d1.cards, d1.shuffled() )

  def test_deck_interface_build_deck(self):
    rules = {
      "suit_rules":[
        (1,"bar","red"),(2,"fuz","blue"),(2,"dez","pink"), ],
      "card_rules":[
        (1,"fish",1),(2,"dog",1),(3,"cat",2),]
      }
    d = Deck(
        unique_cards=False,
        deck_rules=rules )

    self.assertIs( type( d.get_cards() ), list )
    for i in d.cards:
      self.assertIsInstance( i, Card )

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

if __name__=="__main__":
  unittest.main()
