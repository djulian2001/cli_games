from app.card_game import Card_Game 

class Seeds_Card_Game(object):
  """SEEDING for REUSE:"""
  
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

    cg = Card_Game(
      name=cg_name,
      description=cg_description,
      players=["max","brit","Rosco"],
      card_game_rules=cg_card_game_rules )

    return cg

