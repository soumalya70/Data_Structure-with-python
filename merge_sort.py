def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j < m+n:
        if i==m:
            C.append(B[j])
            j=j+1
        elif j==n:
            C.append(A[i])
            i=i+1
        elif A[i]<=B[j]:
            C.append(A[i])
            i=i+1
        elif A[i]>B[j]:
            C.append(B[j])
            j=j+1
    return C
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        mid = len(seq) // 2
        left_half = seq[:mid]
        right_half = seq[mid:]
        left_sorted = merge_sort(left_half)
        right_sorted = merge_sort(right_half)
        return merge(left_sorted, right_sorted)


l=int(input("enter the length of the array: "))
arr=[]
for i in range(l):
    elements=int(input(f"{i+1} element : "))
    arr.append(elements)
print(merge_sort(arr))                 