from first_occurrence_in_array import first_occurrence
from last_occurrence import last_occerrence
# O(n)
# def count_occurrence(arr,x):
#     count=0
#     for i in range(len(arr)):
#         if arr[i] == x:
#             count+=1
#     return count
# print(count_occurrence([1,2,2,2,3,3,4],2))

def count_occurrence(arr,x):
    f=first_occurrence(arr,x)
    if f==-1:
        return 0
    else:
        return (last_occerrence(arr,x)-f)+1
    
print(count_occurrence([1,2,2,2,3,3],2))