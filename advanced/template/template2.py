from string import Template

class MyTemplate(Template):
	delimiter = '#'

def Main():
	cart = []
	cart.append(dict(item="Coke", price=8, qty=2))
	cart.append(dict(item="Cake", price=12, qty=1))
	cart.append(dict(item="fish", price=23, qty=4))
	
	t = MyTemplate("#qty x #item = #price")
	total = 0
	print "Cart:"
	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "Total: " + str(total)

if __name__ == "__main__":
	Main()
