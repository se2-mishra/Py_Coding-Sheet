n1=input('Enter name of the first person:')
n2=input('Enter name of the second person:')
print('Birth year')
a=int(input('Enter for first person:'))
b=int(input('Enter for second person:'))
print('Birth month')
e=int(input('Enter for first person:'))
f=int(input('Enter for second person:'))
print('Birth date')
c=int(input('Enter for first person:'))
d=int(input('Enter for second person:'))

if (a>b):
    print(n1,'is elder than',n2)
elif (a<b):
    print(n2,'is elder than',n1)
else:
    if (e>f):
        print(n2,'is elder than',n1)
    elif (e<f):
        print(n1,'is elder than',n2)
    else:
        if (c>d):
            print(n2,'is elder than',n1)
        else:
            print(n1,'is elder than',n2)
