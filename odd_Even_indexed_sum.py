a=input("Enter elements: ")
n=len(a)
even=0
odd=0
for i in range(n):
    if i%2==0:
        even+=a[i]
    else:
        odd+=a[i]
print("Sum of even terms:",even)
print("sum of odd terms: ",odd)
