
L=['Saturday','Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday']
print("Do you want to get the day of the date")
choice=input("Enter your choice(yes/No):")
top="yes"
gm="y"
while choice.upper()==top.upper() or choice.upper()==gm.upper():
    d=int(input("Enter day's number of the month:"))
    m=int(input("Enter number of month:"))
    y=int(input("Enter the year:"))
    if d==1:
        m=13
        y=y-1
                                                  
        a=int(y/400)
        b=int(y/100)
        c=int(y/4)
        e=int(3*(m+1)/5)
        N= d + 2*m + e + y + c - b + a + 2
    else:
        a=int(y/400)
        b=int(y/100)
        c=int(y/4)
        e=int(3*(m+1)/5)
        N= d + 2*m + e + y + c - b + a + 2
    r=N%7
    p=int(r)
    print('The day of that date is',L[p])
    choice=input("Do you want to continue(yes/no):")
else:
    print("Thanks")
