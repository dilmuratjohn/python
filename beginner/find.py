#little exercise for RegExp in Python
def find_start_imooc(fname):
    f = open (fname)
    for line in f :
        if line.startswith('imooc'):
            print(line)
def find_in_imooc(fname):
    f = open(fname)
    for line in f:
        if line.startswith('imooc') \
         and line[:-1].endswith('imooc'):
            print (line)
find_in_imooc('imooc.txt')


import re

# 创建字符串
str1 = 'www.97568286@qq.com'
str2 = 'fuck imoocc'
# 生成规则
change1 = re.compile(r'[w]{3}.[\w]{1,10}@[\w]{1,5}.com|cn')
change2 = re.compile(r'[\w]*[\s]*imooc')
# 查看规则类型
print(type(change1))
print(type(change2))
# 匹配目标
str1_match = change1.match(str1)
str2_match = change2.match(str2)
# 保存目标
receive_str1_match = str1_match.group()
receive_str2_match = str2_match.group()
# 打印目标
print (receive_str1_match)
print (receive_str2_match)
