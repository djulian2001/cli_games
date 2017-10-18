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
    war.status()
    
  clear_screen()
  player_names = []
  round_index = 0

  for i in range( Card_Game_War.total_players ):
    player_names.append( input( "Enter player {player} name: ".format( player = i+1 ) ) )
  
  war = Card_Game_War( player_names )
  war.deal_cards()

  while war.win() == False:
    new_turn = True
    war_time = 3
    round_index += 1

    # print_status()
    while new_turn != False:
      turn_state=[]
      for player in war.players:
        # print("{name}\'s turn".format( name = player.name ) )
        # print("option\taction")
        # print("------------------")
        # war.turn_choice()
        # choice = int(input("make your choice: "))
        if war.check_player_is_out( player ) == True:
          war.player_takes_pot( war.players[0] )
          win_print( war )
          war.exit_game()

        choice = 1
        if choice != 9:
          turn_state.append( ( player, war.turn( player, choice ) ) )
        else:
          war.exit_game()

      # print("{playerone}'s card {cardone}\n{playertwo}'s card {cardtwo}\n".format(
        # playerone=turn_state[0][0].name,
        # cardone=turn_state[0][1][1],
        # playertwo=turn_state[1][0].name,
        # cardtwo=turn_state[1][1][1] ) )

      compared = war.compare_cards( turn_state )
      if compared is not None:
        # print("{name} takes the turn!".format(name=compared.name))
        war.player_takes_pot(compared)
        new_turn=False
      else:
        # print("IT is War!")
        try:
          war.it_is_war( war_time )
          war_time = 1
        except IndexError as e:
          break
        
  win_print( war )
  
if __name__ == '__main__':
  main()