from app.abc_card_game import ABC_Card_Game

class Test_ABC( ABC_Card_Game ):
	
	def __init__(self):
		# print("Init'ed the class.")
		super().__init__()

	def turn(self):
		# print("In the class method.")
		pass
