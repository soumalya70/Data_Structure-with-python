def binary_search(arr,s,e,x):
    # s=0
    # e=(len(arr))-1
    if s>e:
        return False
    mid=(s+e)//2
    if arr[mid]==x:
        return True
    elif arr[mid]>x:
        return binary_search(arr,s,mid-1,x)
    elif arr[mid]<x:
        return binary_search(arr,mid+1,e,x)
    
print(binary_search([1,2,3,4,5,6,7],0,6,1))