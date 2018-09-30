#!/usr/bin/env python3
import re
stat={}
with open("news.txt") as f:
	for line in f:
		#for word in line:
		words = re.findall(r"(\w+)", line)
		for word in words:
			if word in stat:
				stat[word] += 1
			else:
				stat[word] = 1
	print(stat)
