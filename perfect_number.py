class Solution:
    def isPerfectNumber(self, N):
        # code here 
        a=[]
        for i in range(1,N+1):
            if N%i==0:
               a.append(i)
        if len(a)==0:
            return 0
        j=len(a)-1
        sum=0
        while j!=0:
            sum+=a[j-1]
            j-=1
        if sum==N:
            return 1
        else:
            return 0
        # print(sum)
obj1=Solution()
print(obj1.isPerfectNumber(10))