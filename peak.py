def peak(arr,n):
    l=[]
    for i in range(2,n):
        if arr[i-1]>arr[i-2] and arr[i-1]>arr[i]:
            l.append(arr[i-1])
    return min(l)
print(peak([1,3,2,5,6,4,8],7))