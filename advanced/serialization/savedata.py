import pickle
import Player

items = ["axe", "sword", "gun"]
myObj = Player.Player(1, "Collin", 100.00, items)

print myObj

with open("save2.pkl", "wb") as outfile:
	pickle.dump(myObj, outfile)

print "-" * 9

newObj = None

with open("save2.pkl", "rb") as infile:
	newObj = pickle.load(infile)

print newObj
