r=float(input('Enter radius:'))
print('1. Calculate Area')
print('2. Calculate Circumference')
c=int(input('Enter your choice (1 or 2) to find area or circumference:'))
if c==1:
    ar=3.14*r**2
    print('Area of the circle of radius',r,'is',ar)
elif c==2:
    circum=2*3.14*r
    print('Circumference of the circle of radius',r,'is',circum)
else:
    print('Invalid choice. Enter only from 1 and 2')       