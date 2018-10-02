#!/usr/bin/env python
# -*- coding: utf-8 -*-
# little exercise for basic Python  
name=raw_input('Please input your name!\n')
print('hello,',name)
age=int(input('Please input your age!\n'))        
if age >= 18:
	print('your age is',age)
	print('you are adult')
else:
	print('your age is',age)
	print('you are not adult')


height = input('your heigth (m) ->')
weight = input('your weight (kg) ->')

height = float(height)
weight = float(weight)

bmi = weight / height ** 2

if bmi < 18.5:
    print('Too thin')
elif bmi < 25:
    print('Great~')
elif bmi < 28:
    print('please lose some fat')
elif bmi <32:
    print('...')
else:
    print('?')
print('your BMI is %.2f' % bmi)
