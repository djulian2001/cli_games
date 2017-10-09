from app.card_game import Card_Game

class Card_Game_War( Card_Game ):

  name              = "War"
  description       = "A game of war!"
  total_players     = 2
  max_team_size     = 1
  cards_per_player  = 26
  rules ={
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

  def __init__( self, players ):

    Card_Game.__init__( self,
      name = Card_Game_War.name,
      description = Card_Game_War.description,
      total_players = Card_Game_War.total_players,
      max_team_size = Card_Game_War.max_team_size,
      card_game_rules = Card_Game_War.rules,
      players = players )


  def deal_cards(self):
    super().deal_cards( cards_per_player = Card_Game_War.cards_per_player )

  

