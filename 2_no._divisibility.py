a=float(input('Enter First number:'))
b=float(input('Enter Second number:'))
if a==0 or b==0:
    print("don't enter zero(0)")    
if (a%b or b%a):
    if (a%b==0):
        print(a,'is divisible by',b,'(first  number is divisible by second number)')
    elif (b%a==0):
        print(b,'is divisible by',a,'(second number is divisible by first number)')
    else:
        print("The numbers are co-prime")
else:
    print('Do not enter 0')            
            

    