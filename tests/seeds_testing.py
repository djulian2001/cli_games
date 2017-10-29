from app.card_game import Card_Game
from app.card_game_war import Card_Game_War

from app.player import Player
from app.deck import Deck

class Seeds_Card_Game(object):
  """SEEDING for REUSE of card game objects"""
  
  def seed_a_card_game(self):
    cg_card_game_rules ={
      "game_rules":[(1,"rule 1",5)],
      "deck_rules":{
        "main":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1)] 
        }, }, }

    p1 = Player('Teddy')
    p2 = Player('Ruxin')
    
    players_list= [ p1, p2 ]

    return Card_Game(
      name='adding',
      description='add players',
      players=players_list,
      card_game_rules=cg_card_game_rules )
  
  def seed_a_default_dealt_card_game(self):
    cg = self.seed_a_card_game()

    cards_dealt_each_player = 3
    cards_dealt_each_rotation = 1
    deal_from_deck='main'

    cg.deal_cards( 
      cards_per_player=cards_dealt_each_player,
      per_loop=cards_dealt_each_rotation,
      deck=deal_from_deck,
      position="top" )

    return cg

  def seed_a_card_game_poker_deck(self):
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

    p1 = Player('max')
    p2 = Player('brit')
    p3 = Player('Rosco')
    players_list= [p1,p2,p3]

    cg = Card_Game(
      name=cg_name,
      description=cg_description,
      players=players_list,
      card_game_rules=cg_card_game_rules )

    return cg

class Seeds_Players(object):
  """SEEDING for REUSE of player objects"""

  def seed_player(self, name='Teddy'):
    p = Player(
      name = name,
      computer = True )

    return p

class Seeds_Decks(object):
  """SEEDING for REUSE of deck objects"""
  RULES = {
      "suit_rules":[
        (1,"bar","red"),(2,"fuz","blue"),(2,"dez","pink"), ],
      "card_rules":[
        (1,"fish",1),(2,"dog",1),(3,"cat",2),] }
  
  def seed_deck( self, rules=RULES, unique=False ):
    return Deck( unique_cards=unique, deck_rules=rules )

class Seeds_Card_Game_War(object):
  """docstring for Seeds_Card_Game_War"""
  PLAYER_LIST = [ 'alex','pete' ]
  def seed_a_card_game_of_war( self, player_list = PLAYER_LIST ):
    # so far the game only should require a list of string values for player names
    players_list = [ Player( name=player_name ) for player_name in player_list ]
    return Card_Game_War( players = players_list )
