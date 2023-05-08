alist=['Hello', 'this', 'Is', 'an', 'Example','with', 'cased', 'letters']
n=len(alist)
for i in range(n):
    for j in range(0,n-1):
        if alist[0]>alist[j+1]:
            alist[0],alist[j+1]=alist[j+1],alist[0]
print("List after sorting: ",alist)
