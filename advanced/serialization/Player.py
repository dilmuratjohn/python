class Player:
	
	def __init__(self, Id, Name, Health, Items):
		self.id = Id
		self.name = Name
		self.health = Health
		self.items = Items

	def __str__(self):
		return "My Id: [" + str(self.id) + "]\n"+ \
		       "My Name: [" + str(self.name) + "]\n" +\
		       "My Health: [" + str(self.health) + "]\n" +\
               "My Items: [" + str(self.items) + "]"
