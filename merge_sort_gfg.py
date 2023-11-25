def merge(arr,l,m,r):
    left=arr[l:m+1]
    right=arr[m+1:r+1]
    i=0
    j=0
    k=l
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            k+=1
            j+=1
            
    while i<len(left):
        arr[k]=left[i]
        k+=1
        i+=1
    while j<len(right):
        arr[k]=right[j]
        k+=1
        j+=1

def merge_sort(arr,l,r):
    if r>l:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)


l=[10,5,30,7,15]
merge_sort(l,0,4)
print(l)