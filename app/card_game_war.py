from app.card_game import Card_Game
from app.abc_card_game import ABC_Card_Game

from app.utilities import clear_screen


# class Card_Game_War( Card_Game, ABC_Card_Game ):
class Card_Game_War( Card_Game, ABC_Card_Game ):

  name              = "War"
  description       = "A game of war!"
  total_players     = 2
  max_team_size     = 1
  cards_per_player  = 26
  rules ={
      "game_rules":{
        "turn_options":[ (1,"flip a card"), (9,"quit the game") ] },
      "deck_rules":{
        "main":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red"),(3,"diamonds","red"),(4,"clubs","black")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1),(4,"jack",1),(5,"ten",1),(6,"nine",1),(7,"eight",1),(8,"seven",1),(9,"six",1),(10,"five",1),(11,"four",1),(12,"three",1),(13,"two",1)] 
        },
        "other":{
          "suit_rules":[(1,"spades","black"),(2,"hearts","red"),(3,"diamonds","red"),(4,"clubs","black")],
          "card_rules":[(1,"ace",1),(2,"king",1),(3,"queen",1),(4,"jack",1),(5,"ten",1),(6,"nine",1),(7,"eight",1),(8,"seven",1),(9,"six",1),(10,"five",1),(11,"four",1),(12,"three",1),(13,"two",1)] 
        }, }, }
  win_condition = lambda hands: True if 0 in hands else False

  def __init__( self, players ):
    
    super().__init__(
      name = Card_Game_War.name,
      description = Card_Game_War.description,
      total_players = Card_Game_War.total_players,
      max_team_size = Card_Game_War.max_team_size,
      card_game_rules = Card_Game_War.rules,
      players = players )

  def compare_cards( self, a_round ):
    """
      Takes in a list of 2 items, each item is a tuple of a player and a turn result tuple
        result tuple is rank, card string
      @a_round is the results of 2 turns, 1 for each player
      returns player object if their turn result has the lowest rank, else None
    """
    if a_round[0][1][0] != a_round[1][1][0]:
      return min( a_round, key = lambda rank:rank[1][0] )[0]
    else:
      return None

  def deal_cards(self):
    self.decks['main'].shuffled()
    super().deal_cards( cards_per_player = Card_Game_War.cards_per_player )

  def it_is_war(self, cards):
    """
      a specific condition to the game war, a variable number of cards, 1 or 3, are put
        into the pot by each player.
      @cards int of 1 or 3 value
    """
    def loop_cards( player, loops ):
      for i in range(loops):
        self.add_card_to_pot( player.remove_from_hand( position='top' ) )

    for player in self.players:
      if len( player.hand ) < cards:
        loop_cards( player, len( player.hand ) )
      else:
        loop_cards( player, cards)       

  def status(self):
    """
      Abstract base class requirement:
      This is an observable state of the game
      returns a formated string
    """
    return super().get_game_state()

  def turn(self, player, choice ):
    if choice == 1:
      return super().player_puts_card_in_pot( player, position='top' )
    elif choice == 9:
      self.exit_game()
    else:
      raise TypeError

  def turn_choice(self):
    for choice in super().get_turn_options():
      out_choice = "{id}\t{name}".format( id=choice[0], name=choice[1] )
      print(out_choice)

  def who_won(self):
    """Should return the player that has all the cards or doesn't have zero cards"""
    for player in self.players:
      if len( player.hand ) != 0:
        return player

  def win(self):
    """
      Abstract base class requirement:
      This should be the only method required to call to check if a games win conditions
        have been met
      returns a boolean, True as win conditions have been met, False they have not
    """
    hands_state = ( len(player.hand) for player in self.players )
    return super().check_win_condition( Card_Game_War.win_condition, hands_state )
