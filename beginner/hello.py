#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# little exercise for basic Python  
name=input('Please input your name!\n')
print('hello,',name)
age=int(input('Please input your age!\n'))        
if age >= 18:
	print('your age is',age)
	print('you are adult')
else:
	print('your age is',age)
	print('you are not adult')





#身高体重数据录入
height = input('悄悄告诉我你的身高(m)是：')
weight = input('悄悄告诉我你的体重(kg)是：')
#将srt数据转换成浮点数
height = float(height)
weight = float(weight)
#计算BMI指数
bmi = weight / height ** 2
#输出结果
if bmi < 18.5:
    print('你这样瘦下去会GG的')
elif bmi < 25:
    print('你的体重控制的不错~')
elif bmi < 28:
    print('你这样胖下去会GG的')
elif bmi <32:
    print('我服了Orz')
else:
    print('我已无Fuck说')
print('你的BMI指数是%.2f' % bmi)
