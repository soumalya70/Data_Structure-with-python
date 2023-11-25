def gcd(m,n):
    cf=[]
    for i in range (1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
    #         cf.append(i)
            mrcf=i
    # return cf[-1]
    return mrcf
m=int(input("1st number: "))
n=int(input("2nd number: "))
print(gcd(m,n))