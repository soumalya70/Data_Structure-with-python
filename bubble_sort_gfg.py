def bubble(l):
    n=len(l)
    for i in range(n-1):
        swapped =False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped = True
        if swapped==False:
            return 
    # return l
n=int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    l.append(int(input(f"enter {i+1} element: ")))  
bubble(l)
print(l) 
