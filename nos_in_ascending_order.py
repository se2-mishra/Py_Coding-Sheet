x=float(input('Enter first number:'))
y=float(input('Enter second number:'))
z=float(input('Enter third number:'))
min=mid=max=None
if x<y and x<z:
    if y<z:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
elif y<z and y<x:
    if x<z:
        min,mid,max=y,x,z
    else:
        min,mid,max=y,z,x
else:
    if x<y:
        min,mid,max=z,x,y
    else:
        min,mid,max=z,y,x
print('Numbers in ascending order are',min,mid,max)                              