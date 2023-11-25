# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y, m))
# lis=[2,3,4,5,6,]
# print(lis[-1-1])
# Python program to illustrate functions
# can be passed as arguments to other functions
# def shout(text):
# 	return text.upper()

# def whisper(text):
# 	return text.lower()

# def greet(dc):
# 	# storing the function in a variable
# 	greeting = dc("""Hi, I am created by a function passed as an argument.""")
# 	print (greeting)

# greet(shout)
# greet(whisper)

# def searchInsert( nums, target):
#     for i in range(len(nums)):
#         if nums[i]==target:
#     	    j=i
#         elif nums[i]!=target:
#             while(nums[i]<=target):
#                 j=i
#         else:
#             i=i+1
#             j=i
#     return j
# print(searchInsert(nums=[1,3,5,6],target=2))
# n=[2,5,1,7,9,4]
# j=[]
# for i in range((len(n)-1),-1,-1):
#     j.append(n[i])
# print(j)
# def singleNumber(nums):
#     while(len(nums)>0):
#         j=1
#         for i in range(len(nums)):
#             if nums[i]==nums[j]:
#                 j+=1
#             else:
#                 if nums[j]!=nums[j+1]:
#                     return nums[j]
#                 else:
#                     return nums[j+1]
#                 j+=1
# print(singleNumber([4,1,2,1,2]))



# votes=[1,1,2,3,4,1,2,2,3,1]
# ages=[35,13,23,26,12,24,25,17,17,59]
# counts={}

# for i in range(len(ages)):
#     if ages[i]>=18:
#         vote=votes[i]
#         if vote in counts:
#             counts [vote] +=1

#         else:
#             counts[vote]=1

# res=max(counts,key=counts.get)
# print(res)

# n=int(input())
# print(n%42)
# print(n%76)
# print(n%20)


# def findKthFromRight(n, m, k):
#     l = n**m
#     g = str(l)
#     return g[-k]

# T = int(input())
# result = []

# for _ in range(T):
#     # Taking input for each test case
#     n, m, k = map(int, input().split())
    
#     # Calling the function with the provided values
#     result.append(findKthFromRight(n, m, k))

# # Printing each element of the result array on a new line
# for res in result:
#     print(res)

