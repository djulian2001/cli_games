from app.game import Game
from app.deck import Deck
from app.utilities import pop_list_by_position, clear_screen
from abc import ABC, ABCMeta, abstractmethod
# from app.abc_card_game import ABC_Card_Game


class Card_Game( Game ):
  """This is a subclass of Game"""
  def __init__( self,
                name,
                description,
                card_game_rules,
                players,
                total_players=2,
                max_team_size=1 ):
  
    super().__init__( name, description, players, total_players, max_team_size )
    self.decks = { 'main': None, }
    # this would be better if this was a list of Rule() objects or a Rules() object
    self.card_game_rules = self.set_rules( card_game_rules )
    self.pot = []
    self.set_decks()

  def add_card_to_pot( self, card ):
    """
      Takes a card class object and appends it to the pot
      @card is a object of a Card class
    """
    self.pot.append( card )

  def clear_pot(self):
    """ Sets the class pot attribute to an empty list. """
    self.pot = []

  def check_win_condition( self, condition, state ):
    """Required by the ABC card game class."""
    return condition( state )

  def check_player_is_out( self, player ):
    """
      If the player have no cards and they are out.
      @player this should be a loser
      Return True or False
    """
    return True if len(player.hand) == 0 else False

  def deal_cards( self, cards_per_player, per_loop=1, deck='main', position='top' ):
    """
      Required by the ABC card game class.
      deal cards to active players:
        @cards_per_player  as the number of cards each play should get dealt
        @per_loop     as the number of cards each player gets till total is reached
        @deck         as in which deck the cards come from
    """
    total_loops = int( cards_per_player / per_loop )
    remainder_loop = cards_per_player % per_loop
    
    # ??? would this be a good spot to check game config, expected vs generated for deck ???
    for i in range( total_loops ):
      for index, player in enumerate(self.players):
        for a_loop in range( per_loop ):
          player.hand.append( self.get_card_from_deck( deck , position ) )

    if remainder_loop > 0:
      for index, player in enumerate(self.players):
        for a_loop in range( remainder_loop ):
          player.hand.append( self.get_card_from_deck( deck , position ) )

  def get_turn_options( self ):
    """Returns the sub dictionary settings from the game rules"""
    return self.card_game_rules['game_rules']['turn_options']

  def get_card_from_deck( self, deck_name='main', position='top' ):
    """Gets a card from the game deck and returns that card"""
    return pop_list_by_position( self.decks[deck_name].cards, position )

  def get_game_state(self):
    """Required by the ABC card game class."""
    new_line="\n"
    
    status_output="{game} Game Status{n}".format(
      game=self.name.capitalize(),
      n=new_line)

    for player in self.players:
      status_output+="{name} has {cards} cards{n}".format(
        name=player.name,
        cards=len(player.hand),
        n=new_line )

    status_output += "pot has {pot} cards{n}".format(
      pot = len(self.pot),
      n = new_line )
    
    return status_output

  def player_takes_pot( self, player ):
    """Takes in a player and adds the pot to their and clears the pot"""
    player.add_to_hand( self.pot )
    self.clear_pot()

  def player_puts_card_in_pot( self, player, position ):
    """
      A specific state change of a card from a players hand to the card games pot
      @player is a player class object
      @position is a string as top, bottom, or random
      returns a tuple of the card objects attributes
    """
    to_pot_card = player.remove_from_hand( position )
    self.add_card_to_pot( to_pot_card )
    return ( to_pot_card.rank, to_pot_card.__str__() )

  def set_rules(self, rules):
    """Ensures a dictionary structure exists"""
    if 'deck_rules' in rules:
      return rules
    else:
      rules['deck_rules']={}
      return rules

  def set_decks(self):
    """
      This methods job is to set the deck objects for the card_game's decks 
        attribute using the card games deck rules
    """
    # i have to check this because the rules require data structure.
    if 'main' in self.card_game_rules["deck_rules"]:
      for key in self.card_game_rules["deck_rules"]:
        # self.decks[key] = self.build_deck(self.card_game_rules["deck_rules"][key])
        self.decks[key] = Deck( unique_cards=True, deck_rules=self.card_game_rules["deck_rules"][key] )


