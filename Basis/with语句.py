import sys
__author__ = "Colin"

# f = open("yesterday2","r",encoding="utf-8")

with open("yesterday2", "r", encoding="utf-8") as f1,\
     open("yesterday2", "r", encoding="utf-8") as f2:
    for line in f1:
        print(line)

