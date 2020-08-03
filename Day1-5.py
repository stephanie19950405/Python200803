# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:29:05 2020

@author: AE401
"""

x=input("請輸入成績")
x=int(x)
if x >=0 and x <=100:
    print("你的等級是:")
    if x >=90:
        print("A")
    elif x >=80:
        print("B")
    elif x >=70:
        print("C")
    elif x >=60:
        print("D")
    else:
        print("E")
else:
    print("請重新輸入!")