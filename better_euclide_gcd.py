def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    while(m%n)!=0:
        (m,n) = (n,m%n)
    return (n)
m=int(input("1st number: "))
n=int(input("2nd number: "))
print(gcd(m,n))