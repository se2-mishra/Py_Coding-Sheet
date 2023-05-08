print("1. Area of circle")
print("2. Area of square")
print("3. Area of rectangle")
choice=int(input("Choice: "))
if choice==1:
    r=float(input("Enter radius of the circle:"))
    ar=3.14157*r*r
if choice==2:
    a=float(input("Enter the length of the side" ))
    ar=a*a
if choice==3:
    l=float(input("Enter the length of the rectangle: "))
    b=float(input("Enter the breadth of the rectangle: "))
    ar=l*b
print("Area=",ar)
