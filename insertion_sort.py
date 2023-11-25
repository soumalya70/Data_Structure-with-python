def insertion_sort(seq):
    for sliceEnd in range(len(seq)):
        pos=sliceEnd
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos], seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1
    return seq
l=int(input("enter the length of the array: "))
arr=[]
for i in range(l):
    elements=int(input(f"{i+1} element : "))
    arr.append(elements)
print(insertion_sort(arr))