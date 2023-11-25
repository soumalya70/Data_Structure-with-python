# def first_occurrence(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             break
#     return i


# def first_occurrence(arr,s,e,x):
#     if s>e:
#         return -1
#     mid=(s+e)//2
#     if x>arr[mid]:
#         return first_occurrence(arr,mid+1,e,x)
#     elif x<arr[mid]:
#         return first_occurrence(arr,s,mid-1,x)
#     else:
#         if mid==0 or arr[mid-1]!=arr[mid]:
#             return mid
#         else:
#             return first_occurrence(arr,s,mid-1,x)
        
# print(first_occurrence([1,2,2,3,3,3,4,5,5,6,6,6,6,6,7],0,14,6))

def first_occurrence(arr,x):
    s=0
    e=len(arr)-1
    while s<=e:
        mid=(s+e)//2
        if x>arr[mid]:
            s=mid+1
        elif x<arr[mid]:
            e=mid-1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                e=mid-1

# print(first_occurrence([1,2,2,3,3,3,4,5,5,6,6,6,6,6,7],6))