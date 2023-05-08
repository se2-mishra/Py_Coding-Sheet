# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 17:13:34 2021

@author: User
"""

"""

income=float(input("Enter Annual Income( is Rs) : "))           //2
if income > 1000000:
    inc_tax=(0.04)*(income)
    print("Income tax on amount >1000000 : 4% \n")
    print("Income tax : ",inc_tax)
elif (income) > 500000 and income <=1000000:
    inc_tax=(0.02)*(income)
    print("Income tax on amount >500000 and <=1000000 : 2% \n")
    print("Income tax : ",inc_tax)
else:
    print("Income <500000 have no income tax")
    
"""

"""
mark=int(input("Enter Marks : "))                   //3rd
cl_type=input("Enter class type(T/L) : ")
if cl_type in ["T","L"]:
        
    if mark>=80:
        if cl_type=="T":
            t_mark=(0.08)*mark+(mark)
        elif cl_type=="L":
            t_mark=(0.06)*mark+(mark)
    if mark>=60 and mark <80:
        if cl_type=="T":
            t_mark=(0.06)*mark+(mark)
        elif cl_type=="L":
            t_mark=(0.04)*mark+(mark)
    if mark>=40 and mark <60:
        if cl_type=="T":
            t_mark=(0.04)*mark+(mark)
        elif cl_type=="L":
            t_mark=(0.02)*mark+(mark)
    if mark<40:
        if cl_type=="T":
            t_mark=(0.0)*mark+(mark)
        elif cl_type=="L":
            t_mark=(0.00)*mark+(mark)
    
    if mark==0:
        print("Enter Appropriate marks")

else:
    print("Class type not found")


print("Total marks in class type =",cl_type," is =",t_mark)

"""



"""



s=float(input("Enter distance travelled(in KM) :"))             //2
cost=0.0
if s <= 10:
    cost=(15)*(s)
elif s<= 100:
    cost=150 + (s-10)*8
else:
    cost=150+720+(s-100)*6

print("Distance travelled : ",s)
print("Total fare :",cost)
        
"""   


"""
def fact(k):
    
    factorial = 1
    if k < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif k == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,k + 1):
           factorial = factorial*i
       print("The factorial of",k,"is",factorial)
   

num = int(input("Enter Number :"))
print("Factorial of even number")
for j in range(1,num+1):
    if (j%2==0):
        fact(j)
        
print("Factorial of odd number")
for m in range(1,num+1):
    if (m%2!=0):
        fact(m)

"""

number = int(input("Enter number: "))
total_sum = 0
step = 1
condition=True
while condition:
    
    while number:
        total_sum += number%10
        number //= 10
    
    print("Step-",step," Sum: ",total_sum)
    number = total_sum
    total_sum = 0
    step += 1
    condition = number > 9





























