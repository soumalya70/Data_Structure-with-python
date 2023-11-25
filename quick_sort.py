def quicksort(a,l,r):
    if r-l<=1:
        return ()

    yellow=l+1
    
    for green in range(l+1,r):
        if a[green]<=a[l]:
            (a[yellow],a[green])=(a[green],a[yellow])
            yellow=yellow+1
    (a[l],a[yellow-1])=(a[yellow-1],a[l])
    quicksort(a,l,yellow-1)
    quicksort(a,yellow,r)

l=int(input("Enter the length of the array: "))
arr=[]
for i in range(l):
    n=int(input(f'Enter the {i+1} element of the array: '))
    arr.append(n)
quicksort(arr,0,l)
print("Sorted array",arr) 
