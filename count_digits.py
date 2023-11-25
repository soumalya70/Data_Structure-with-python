def count(n):
    cn=0
    while n!=0:
        n=n//10
        cn+=1
    return cn
print(count(9234))