def selectionsort(l):
    n=len(l)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if l[min]>l[j]:
                min=j
        l[min],l[i]=l[i],l[min]
    
n=int(input("Enter the number of elements: "))
l=[]
for i in range(n):
   l.append(int(input(f"{i+1:}: ")))
selectionsort(l)
print(l) 