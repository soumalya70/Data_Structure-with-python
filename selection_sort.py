def selection_sort(seq):
    for start in range (0,len(seq)):
        minpos=start
        for i in range (start,len(seq)):
            if seq[i]<seq[minpos]:
                minpos=i
        (seq[start],seq[minpos])=(seq[minpos],seq[start])
    return seq
l=int(input("enter the length of the array: "))
arr=[]
for i in range(l):
    elements=int(input(f"{i+1} element : "))
    arr.append(elements)
print(selection_sort(arr))
