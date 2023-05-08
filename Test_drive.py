# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:41:55 2019

@author: Relight


def foot(x):
    global inc
    inc=12*x
    return inc

a=float(input("Enter the length in foot:"))
print(foot(a),'inches')
""

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

    a=a-1
    print(Month[a],day,',',year)

a=int(input("Enter date in(MMDDYYYY) form: "))
b=str(a)
c=date_conv(b)
"""

for row in range(1,5):
    for col in range(1,3):
        print(col,end="")
    print()





















    
    
    
    
    
    
    
    
    
    
    
    