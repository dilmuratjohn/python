import pickle

dict1 = {
	'a': 100,
	'b':200,
	'c':300
}

list1 = [
	500,
	700,
	900]

print dict1
print list1

output = open("save1.pkl", "wb")

pickle.dump(dict1, output)
pickle.dump(list1, output)

output.close()

print "-" * 10

inputFile = open("save1.pkl", "rb")

dict2 = pickle.load(inputFile)
list2 = pickle.load(inputFile)

inputFile.close()

print dict2
print list2





