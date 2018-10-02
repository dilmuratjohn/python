#little exercise for RegExp in Python
def find_start_text(fname):
    f = open (fname)
    for line in f :
        if line.startswith('shit'):
            print(line)
def find_in_text(fname):
    f = open(fname)
    for line in f:
        if line.startswith('shit') \
         and line[:-1].endswith('shit'):
            print (line)

import re

str1 = 'www.someone@gmail.com'
str1_match = re.compile(r'[w]{3}.[\w]{1,10}@[\w]{1,5}.com|cn').match(str1).group()
print str1_match

