def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n == 0:
        return(n)
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff)))
m=int(input("1st number: "))
n=int(input("2nd number: "))
print(gcd(m,n))