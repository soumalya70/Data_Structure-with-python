# def binary_search(seq,n,f,l):
#     if f-l==0:
#         return False
#     mid=(f+l)//2
#     if(n==seq[mid]):
#         return True
#     if(n<seq[mid]):
#         return binary_search(seq,n,f,mid)
#     else:
#         return binary_search(seq,n,mid+1,l)
# seq=[]
# n=int(input("Enter the number of elements: "))
# for i in range (n):
#     num=int(input(f"{i+1}th element is: "))
#     seq.append(num)
# s=int(input("Enter the number you want to search: ")) 
# f=seq[0]
# l=seq[-1]
# print(binary_search(seq,n,f,l))

def binary_seacrh(arr,x):
    s=0
    e=(len(arr))-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==x:
            return True
        elif arr[mid]>x:
            e=mid-1
        elif arr[mid]<x:
            s=mid+1
    else:
        return False
print(binary_seacrh([1,2,3,4,5,6,7],4))
        
        