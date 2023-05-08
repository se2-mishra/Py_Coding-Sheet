count,sum=0,0
num=int(input('Enter Number:'))
if num>0:
    for i in [num]:
        count+=1
        sum+=i
        i=num-2
        if count==10:
            print(sum/float(count))
            break