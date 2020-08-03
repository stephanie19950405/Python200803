# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:25:13 2020

@author: AE401
"""

m=input("請輸入數學成績")
e=input("請輸入英文成績")
m=int(m)
e=int(e)
if m >=90 and e >=90:
    print("得到獎品")
elif m <60 or e<60:
    print("再努力")
elif m <60 and e<60:
    print("要處罰")
else:
    print("再加油")