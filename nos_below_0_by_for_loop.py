num=int(input('Enter number:'))
sum=0
min=0
max=num
if num<0:
    min=num
    max=0                                                  #compute sum of integers from minto max
    for i in range(min,max+1):
        sum+=1
        print(i)