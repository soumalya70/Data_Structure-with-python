def gcd(m,n):
    fm=[]
    fn=[]
    cf=[]
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i)   
    for j in range(1,n+1):
        if n%j==0:
            fn.append(j)
               
    for f in fm:
        if f in fn:
            cf.append(f)
    return cf[-1]
m=int(input("1st number: "))
n=int(input("2nd number: "))
print(gcd(m,n))
