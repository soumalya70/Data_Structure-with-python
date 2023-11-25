n=int(input())
arr=[]
for i in range (n):
    arr.append(int(input()))

def partition(arr,l,h):
    p=arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<=p:
            i=i+1
        (arr[i],arr[j])=(arr[j],arr[i])
    (arr[i+1], arr[h])=(arr[h],arr[i+1]
    return  
def quicksort(arr):
    
    for i in range(len(arr)+1):
        if arr[i+1]<arr[i]:
            (arr[i], arr[i+1])=(arr[i+1], arr[i])
    
    return arr
print(quicksort(arr))