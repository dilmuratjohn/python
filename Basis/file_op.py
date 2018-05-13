__author__ = "Colin"

f = open("yesterday.txt", 'r',  encoding="utf-8")  # 文件句柄
data0 = f.read()
data2 = f.read()
print('-----data0-----\n', data0)
print('-----data2-----\n', data2)  # 因为有文件指针
f.close()

f = open("yesterday2.txt", 'w',  encoding="utf-8")
f.write("\nwhen i was young i listen to the radio\n")
f.close()

f = open("yesterday2.txt", 'r',  encoding="utf-8")
print(f.tell())
data1 = f.read()
print('-----read-----\n', data1)
print(f.tell())
f.seek(0)
data3 = f.read()
print('-----read-----\n', data3)
f.close()

# f = open("yesterday2",'r+', encoding="utf-8")  # 文件句柄 读写
# f = open("yesterday2",'w+', encoding="utf-8")  # 文件句柄 写读
# f = open("yesterday2",'a+', encoding="utf-8")  # 文件句柄 追加读写
# f = open("yesterday2",'wb')  # 文件句柄 二进制文件

# f.write("hello binary\n".encode()) # 写二进制

# print(f.encoding)
# print(f.flush())
# print(dir(f.buffer))

'''
#high loop

count = 0
for line in f:
    if count == 9:
        print('-----我是分割线-----')
        count += 1
        continue
    print(line)
    count +=1

#low loop

for index,line in enumerate(f.readlines()):
    if index == 9:
        print('-----我是分割线-----')
        continue
    print(line.strip())
#for i in range(5):
#    print(f.readline())
'''
