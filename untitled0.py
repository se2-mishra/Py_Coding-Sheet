# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:29:25 2019

@author: Z
"""


"""Write a program in python to check a number whether it is prime or not."""
num=int(input("Enter the number: "))
for i in range(2,num):
    if num%i==0:
        print(num, "is not prime number")
        break
    else:
        print(num,"is prime number")