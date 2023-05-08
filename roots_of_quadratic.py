import math
print('For quadratic Equation,ax**2+bx+c=0,enter coefficients below')
a=int(input('Enter "a" of the equation:'))
b=int(input('Enter "b" of the equation:'))
c=int(input('Enter "c" of the equation:'))
if a==0:
    print('Value of',a,'should not be zero')
    print('\n Aborting !!!!!!')
else:
    d=b**2-4*a*c
    if d>0:
        alpha=(-b+math.sqrt(d))/(2*a)
        beta=(-b-math.sqrt(d))/(2*a)
        print('Roots are REAL but UNEQUAL')
        print('First root=',alpha)
        print('Second root=',beta)
    elif d==0:
        alpha=beta=-b/(2*a);
        print('Roots are REAl and EQUAL')
        print('First root=',alpha)
        print('Second root=',beta)
    else:
        print('Roots are COMPLEX and IMAGINARY')        
                
        
        
        