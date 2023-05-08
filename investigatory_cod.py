# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:09:34 2019

@author: Setu\
"""
import tkinter

def add():
    
    choice=input("Do u want to add a new student(Y/N):")
    if choice=="Y":
    
        a=input("Enter the path(Where u wanna save the details):")  
        while choice=="Y":
        
            n=input("Enter student name:")
            n=a+n
            m=n+".txt"
            f=open(m,"w+")
            roll=input("Enter roll no:")
            cl=input("Enter Class:")
            age=input("Enter age:")
            f=open(m,'a')
            roll="Roll Number:"+roll+"\n"
            cl="Class:"+cl+"\n"
            age="Age:"+age+"\n"
            f.write(n)
        
            f.write(roll)
            f.write(cl)
            f.write(age)
            choice=input("Do u want to add a new student(Y/N):")
        f.close()
        
    
    
    

    