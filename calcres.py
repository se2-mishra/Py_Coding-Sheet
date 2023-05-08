# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 11:20:12 2019

@author: User
"""

def calcresult():
    i=10
    while i>1:
        if 1%3==0:
            x=1%3
            i=i-1
        else:
            i=i-3
            x=i
        print(x**3)
calcresult()