sum=int(input())
size=int(input())
arr=list(map(int,input().split()))


arr.sort()
print(arr)
if size<2:
    print(-1)
for i in range(len(arr)):
    if arr[i]+arr[i+1]<sum:
        print(arr[i]*arr[i+1])
        break
    else:
        print(0)
