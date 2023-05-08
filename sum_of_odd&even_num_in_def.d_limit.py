n=int(input('Enter the limit:'))
ctr=0
even=odd=0
while ctr<=n:
    if ctr%2==0:               #For even number
        even+=ctr
    else:
        odd+=ctr
    ctr+=1                       #Increment the counter     
print('The sum of even number is',even)
print('The sum of the odd number is',odd) 