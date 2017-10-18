from app.player import Player
from app.utilities import clear_screen
import sys

class Game(object):
  """a bit high level but i'm woriking on inheratance"""
  def __init__(self,name,description,players,total_players=2,max_team_size=1):
    self.name = name
    self.description = description
    self.players = self.set_players( players )
    self.players_out = []
    self.total_players = total_players
    self.max_team_size = max_team_size
    self.total_teams = self.get_total_teams()

    # self.rules = { Rule(), Rule(), ... }

  def get_total_teams(self):
    return int(self.total_players/self.max_team_size) + (self.total_players % self.max_team_size > 0)

  def set_players(self, players):
    return [ Player( name=player ) for player in players ]

  def get_player_by_name( self, name ):
    """
      Returns a player object from the players list
      @name as a string
      returns Player object
      NOTE: might be better as a Game method
    """
    for player in self.players:
      if name == player.name:
        return player

  def exit_game(self):
    # clear_screen()
    # print("Thanks for playing!")
    sys.exit(1)