# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:47:47 2019

@author: User
"""

conv=0.621371
lim=int(input("Enter the extent of conversion: "))
print("Miles",     '          ','Kilometres'    )
for row in range(1,lim+1):
    for col in range(1,2):
        i=row/conv
        print(row,     '          '    ,i)
print()
print()
conv=2.2        
print("Pounds",     '          ','Kilograms'    )
for row in range(1,lim+1):
    for col in range(1,2):
        i=row/conv
        print(row,     '          '    ,i)