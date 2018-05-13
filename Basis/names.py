# Author:Colin
import copy
names = ["1ZhangYang", "@XiangPeng", "XiangPeng", "GuYun", "XuLiangChen"]

#names3 = names.copy()  #浅copy
#names3=copy.copy(names)
#names3=names[:]
#names3=list(names)
names4 = copy.deepcopy(names)  #深copy

print(names)
print(names3)
print(names4)
# print(names[0], names[1])
# print(names[1:3])
# print(names[-3:-1])  # 顾头不顾尾

# names.append("'LeiHaiDong")

# names.insert(1, "DiLi")

# names[2] = "XieDi"

# #del names[1] = names.pop(1)

# names.pop()

# print(names[names.index("XieDi")])
#
# print(names.count("XiangPeng"))
#
# # names.clear()
#
# names.reverse()
#
# names.sort()
#
# print(names)
#
# names2 = [1, 2, 3, 4]
# names.extend(names2)
# print(names,names2)

