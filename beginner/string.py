# Author:Colin

name = "my \tname is {name} and i am {year} old"

print(name.capitalize())
print(name.count("a"))
print(name.center(50, "-"))
print(name.endswith("me"))
print(name.expandtabs(tabsize=30))
print(name[name.find("name"):])
print(name.format(name="alex", year=23))
print(name.format_map({'name': 'alex', 'year': 23}))
print('123'.isalnum())
print('fff'.isalpha())
print('11'.isdecimal())
print('1A'.isdigit())
print('a@'.isidentifier())  #判断是否为合法变量名
print('+'.join(['1', '2', '3', '4']))
print(name.ljust(50, '#'))
print(name.rjust(50, '#'))
print('   \nAlex   \n'.strip())

p = str.maketrans('abcdefghijklmn', '1^#$5678^*^234')
print("colin is i".translate(p))

print('all alex'.replace('l', 'L', 1))
print('alex lol'.rfind('l'))
print('1+2+3+4'.split('+'))
print('1+2\n3+4'.splitlines())
print('Alex Di'.swapcase())
print('lex di'.zfill(50))

