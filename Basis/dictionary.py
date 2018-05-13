# Author:Colin
#key-value


av_catalog = {
    "欧美":{
        "www.y.com": ["a","b"],
        "www.p.com": ["a","b"],
        "letmedothistoyou.com": ["a","b"],
        "x-art.com":["a","b"]
    },
    "日韩":{
        "tokyo-hot":["a","b"]
    },
    "大陆":{
        "1024":["a","b"]
    }
}

av_catalog["大陆"]["1024"][1] = "abcd"

av_catalog.setdefault("大陆",{"www.baidu.com":[1,2]})
print(av_catalog)




info = {
    'stu1101': "Tenglan Wu",
    'stu1102': "Luola Longze",
    'stu1103': "Maliya Xiaoze",
}

print(info.get('stu1104'))
print('stu1103' in info)  #info.has_key("1103") in python2.x

print(info)














# info["stu1101"] = "武藤兰"
# info["stu1104"] = "cang"

# info.pop('stu1101')
# info.popitem()
# del info["stu1104"]

# print(info)