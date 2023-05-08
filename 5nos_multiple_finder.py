import pdb
pdb.set_trace()
print('Enter five numbers to check the divisibility')
a=float(input('Enter First number:'))
b=float(input('Enter Second number:'))
c=float(input('Enter Third number: '))
d=float(input('Enter Fourth number: '))
e=float(input('Enter Fifth number: '))
div=float(input('Enter divisor number'))
count=0
print('Multiples of',div,'are:')
r=a%div
if r==0:
    print(a,sep='')
    count+=1
r=b%div
if r==0:
    print(b,sep='')
    count+=1
r=c%div
if r==0:
    print(c,sep='')
    count+=1
r=d%div
if r==0:
    print(d,sep='')
    count+=1
r=e%div
if r==0:
    print(e,sep='')
    count+=1
print()
print('There are',count,'multiples of',div,'found')                
    
