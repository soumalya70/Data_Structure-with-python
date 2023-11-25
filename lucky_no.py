class Solution:
    def isLucky(self, n): 
        
        i=1
        while i<=n:
            arr=[]
            for j in range(1,i,n+1):
                arr.append(j)
            i+=1
        return (len(arr))
obj1= Solution()
obj1.isLucky(5)