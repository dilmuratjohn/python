import re
stat={}
with open("news.txt") as f:
	for line in f:
		#for word in line:
		words = line.split(" ")	
		words = re.findall(r"(\w+)", line)
		print(words)
		for word in words:
			print(word)
			if word in stat:
				stat[word] += 1
			else:
				stat[word] = 1
	print(stat)
