def merge(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i]>b[j]:
            res.append(b[j])
            j+=1
        else:
            res.append(a[i])
            i+=1
    while i<m:
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1
    return res
print(merge([1,2,3,4,5,6],[4,9,10,11,12]))