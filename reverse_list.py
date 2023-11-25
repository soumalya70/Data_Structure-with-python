def revlist(l):
    s=0
    e=len(l)
    b=0
    while(s<e):
        # b=l[s]
        # l[s]=l[e-1]
        # l[e-1]=b
        l[s],l[e-1]=l[e-1],l[s]
        s+=1
        e-=1
    return l
L=[int(x) for x in input().split(',')]
print(revlist(L))