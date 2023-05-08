# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 13:59:06 2019

@author: Zabojca
"""

def sum(a,b,c,d):
    result=0
    result=result+a+b+c+d
    return result

def length():
    return 4

def mean(a,b,c,d):
    return float(sum(a,b,c,d))/length()

print(sum(a,b,c,d), length())     