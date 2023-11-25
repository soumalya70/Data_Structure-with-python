def issorted(l):
    if len(l)<=1:
        return True
    i=1
    while(i<len(l)):
        if l[i]<l[i-1]:
            return False
        i=i+1
        
        return True
l=[int(x) for x in input().split()]
print(issorted(l))