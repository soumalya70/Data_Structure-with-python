def insertionSort(seq):
    isort(seq,len(seq))
    return seq
def isort(seq,k):
    if k>1:
        isort(seq,k-1)
        insert(seq,k-1)
def insert(seq,k):
    pos=k
    while pos>0 and seq[pos]<seq[pos-1]:
        (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
        pos=pos-1
l=int(input("enter the length of the array: "))
arr=[]
for i in range(l):
    elements=int(input(f"{i+1} element : "))
    arr.append(elements)
print(insertionSort(arr))  