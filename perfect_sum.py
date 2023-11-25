n=int(input())
i=1
count=0
for i in range(n+1):
    for j in range(i):
        if i**2+j**3<n:
            count+=1
        elif i**3+j**2<n:
            count+=1
print(count)