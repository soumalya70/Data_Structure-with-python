
# O(n)
# def last_occerrence(arr,x):
#     for i in range((len(arr)-1),0,-1):
#         if arr[i] == x:
#             return i
#     return -1
# print(last_occerrence([1,2,3,3,4,5,5,6],5))

# o(logn) aux=o(logn) recursive
# def last_occerrence(arr,low,high,x):
#     if low > high:
#         return -1
#     mid=(low+high)//2
#     if x>arr[mid]:
#         return last_occerrence(arr,mid+1,high,x)
#     elif x<arr[mid]:
#         return last_occerrence(arr,low,mid-1,x)
#     else:
#         if mid==len(arr)-1 or arr[mid+1]!=arr[mid]:
#             return mid
#         else:
#             return last_occerrence(arr,mid+1,high,x)
# print(last_occerrence([1,2,3,3,4,5,5,6],0,7,5))


# o(logn) aux=o(1)
def last_occerrence(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if x>arr[mid]:
            low=mid+1
        elif x<arr[mid]:
            high=mid-1
        else:
            if mid==len(arr)-1 or arr[mid+1]!=arr[mid]:
                return mid
            else:
                low=mid+1    
        
        
        [5,10,10,10,6]