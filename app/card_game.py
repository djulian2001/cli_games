from app.game import Game
from app.deck import Deck
from app.utilities import pop_list_by_position

class Card_Game( Game ):
  """This is a subclass of Game"""
  def __init__(
      self,
      name,
      description,
      card_game_rules,
      players,
      total_players=2,
      max_team_size=1 ):
    
    Game.__init__(self, name, description, players, total_players, max_team_size)
    self.decks = { 'main': None, }
    # this would be better if this was a list of Rule() objects or a Rules() object
    self.card_game_rules = self.set_card_game_rules( card_game_rules )
    self.pot = []
    self.set_decks()

  def set_card_game_rules(self, rules):
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
        self.decks[key] = self.build_deck(self.card_game_rules["deck_rules"][key])

    
  def build_deck(self,deck_rules):
    a_deck = Deck(
      unique_cards=True,
      deck_rules=deck_rules )
    return a_deck


  def deal_cards( self, total_cards, per_loop=1, deck='main', position='top' ):
    """
      deal cards to active players:
        @total_cards  as the number of cards each play should get dealt
        @per_loop     as the number of cards each player gets till total is reached
        @deck         as in which deck the cards come from
    """
    total_loops = int( total_cards / per_loop )
    remainder_loop = total_cards % per_loop
    
    # ??? would this be a good spot to check game config, expected vs generated for deck ???
    for i in range( total_loops ):
      for index, player in enumerate(self.players):
        for a_loop in range( per_loop ):
          player.hand.append( self.get_card_from_deck( deck , position ) )

    if remainder_loop > 0:
      for index, player in enumerate(self.players):
        for a_loop in range( remainder_loop ):
          player.hand.append( self.get_card_from_deck( deck , position ) )


  def get_card_from_deck( self, deck_name='main', position='top' ):
    """Gets a card from the game deck and returns that card"""
    return pop_list_by_position( self.decks[deck_name].cards, position )

  def get_player_by_name( self, name ):
    for player in self.players:
      if name == player.name:
        return player

  def player_takes_pot( self, player ):
    """Takes in a player and adds the pot to their and clears the pot"""
    player.add_to_hand( self.pot )
    self.clear_pot()

  def clear_pot(self):
    self.pot = []


  def get_game_status(self):
    new_line="\n"
    
    status_output="{game} Game Status{n}".format(
      game=self.name.capitalize(),
      n=new_line)

    for player in self.players:
      status_output+="{name} has {cards} cards{n}".format(
        name=player.name,
        cards=len(player.hand),
        n=new_line )

    return status_output

