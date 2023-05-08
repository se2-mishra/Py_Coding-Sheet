# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 10:39:41 2019

@author: Zabojca
"""
import random
STRING="CBSEONLINE"
NUMBER=random.randint(0,3)
N=9
while STRING[N] !='L':
    print(STRING[N]+STRING[NUMBER]+'#',end='')
    NUMBER=NUMBER+1
    N=N-1
import random   
X=[100,75,10,125]
Go=random.randint(0,3)
for i in range(Go):
    print(X[i],"$$",end="")
    
import random
POINTS=[20,40,10,30,15]
POINTS=[30,50,20,40,45]
BEGIN=random.randint(1,3)
LAST=random.randint(2,4)
for C in range(BEGIN,LAST+1):
    print(POINTS[C],"#",end='')
