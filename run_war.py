from app.card_game_war import Card_Game_War
from app.utilities import clear_screen
# tdd

def main():
  def win_print( war ):
    print_status()
    winner = war.who_won()
    print( "The winner: {name} in {turns} turns!".format( name=winner.name, turns=round_index ) )

  def print_status():
    # clear_screen()
    print("------------------")
    print( war.status() )
  
  def check_game_state( war ):
    """Player runs out of cards, triggers win for other player and ends game..."""
    # print('p1: {}, p2: {}, pot: {}, at {}'.format(len(war.players[0].hand),len(war.players[1].hand), len(war.pot), round_index ) )
    if war.win():
      for player in war.players:
        if len(player.hand) != 0:
          war.player_takes_pot( player )
      win_print( war )
      war.exit_game()

  clear_screen()
  player_names = []
  round_index = 0

  for i in range( Card_Game_War.total_players ):
    player_names.append( input( "Enter player {player} name: ".format( player = i+1 ) ) )
  
  war = Card_Game_War( player_names )
  war.deal_cards()
  
  while war.win() == False:
    war_time = 3
    round_index += 1
    new_turn = True

    while new_turn != False:
      cards_played = []
      for player in war.players:
        choice = 1
        if choice != 9:
          cards_played.append( ( player, war.turn( player, choice ) ) )
        else:
          war.exit_game()

      check_game_state( war )

      try:
        compared = war.compare_cards( cards_played )  
      except IndexError as e:
        print(compared, cards_played)
        check_game_state( war )

      if compared is not None:
        war.player_takes_pot(compared)
        new_turn=False
      else:
        war.it_is_war( war_time )
        war_time = 1
        check_game_state( war )
       
  win_print( war )
  war.exit_game()
  
if __name__ == '__main__':
  main()