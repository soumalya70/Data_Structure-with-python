
def prime(n):
    # if n==1:
    #     return False
    # for i in range(2,n):
    #     if n%i==0:
    #         return False
    #     else:
    #         return True
            
    if n==1:
        return False
    i=2
    while(i*i<=n):
        if n%i==0:
            return False
        i+=1
    return True
def primefactorization(n):
    i=1
    while(i<=n):
        if prime(i):
            while(n%i==0):
                n=n//i
                print(i, end="  ")
        i+=1

primefactorization(100)
                
            
        