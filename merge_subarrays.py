def merge_subarray(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    i=0
    j=0
    k=low
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            a[k]=left[i]
            k=k+1
            i=i+1
        else:
            a[k]=right[j]
            k=k+1
            j=j+1
    while i<len(left):
        a[k]=left[i]
        k=k+1
        i=i+1
    while j<len(right):
        a[k]=right[j]
        k=k+1
        j=j+1
    return a  
l=merge_subarray([1,5,6,8,2,3,4],0,3,6)
print(l)