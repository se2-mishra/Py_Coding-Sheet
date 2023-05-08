# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:34:10 2019

@author: Relight
"""

Month=['January','February','March','April','May','June','July','August','September','October','November','December']
def date_conv(x):
    
    if len(x)==7:
        year=x[3:7]
        month=x[0]
        day=x[1:3]
        a=int(month)
    if len(x)==8:
        year=x[4:8]
        month=x[0:2]
        day=x[2:4]
        a=int(month)
    a=a-1
    print(Month[a],day,',',year)

a=int(input("Enter date in(MMDDYYYY) form: "))
b=str(a)
c=date_conv(b)
