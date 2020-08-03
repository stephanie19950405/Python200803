# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:56:36 2020

@author: AE401
"""

x=input("請輸入身高")
y=input("請輸入體重")
x=float(x)
y=float(y)
x1=x/100
BMI=y//x1**2
if BMI<18.5:
    print("體重不足")
elif BMI<24:
    print("正常")
elif BMI<27:
    print("過重")
elif BMI<30:
    print("輕度肥胖")
elif BMI<35:
    print("中度肥胖")
else:
    print("過度肥胖")
