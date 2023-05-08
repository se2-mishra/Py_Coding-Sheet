sum1=0
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
su=a+b+c
if (a!=b and a!=c):
    sum1+=a
if (b!=c and b!=a):
    sum1+=b
if (c!=a and c!=b):
    sum1+=c
if (sum1==su):
    print("The number doesn't have any duplicate value")            
    print('The number without duplication is',sum1)
print(a,'+',b,'+',c,'=',su)    
    







