count,sum=0,0
num=int(input('Enter Number:'))
while num>0:
    count+=1
    sum+=num
    num-=2
    if count==10:
        print(sum(float(count)))
        break