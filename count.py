

# votes = [1, 1, 2, 3, 4, 1, 2, 2, 3, 1]
# ages = [35, 13, 23, 26, 12, 24, 25, 17, 17, 59]

# vote_counts = {}

# for i in range(len(votes)):
#     if ages[i] > 18:
#         if votes[i] in vote_counts:
#             vote_counts[votes[i]] += 1
#         else:
#             vote_counts[votes[i]] = 1
            
# max_votes = max(vote_counts.values())
# winning_numbers = []
# for num, count in vote_counts.items():
#     if count == max_votes:
#         winning_numbers.append(num)
# winning_numbers.sort()
# print( winning_numbers[-1])




# def perfect_squre(t):
#     a=[]
#     for i in range(t):
#         a.append(int(input()))
    
#     for i in a:
# #         for j in range(1,i):
# #             if j**2<i:
# #                 d=i-j*2
# #                 e=(j+1*j+1)-i
#         c=0
#         while(c*c<i):
#             d=i-c*c
#             g=((c+1)*(c+1))-i
#             b=c
#             if g==0:
#                 g=((c+2)*(c+2)-i)
#                 break
#             c+=1
        
#         if d<g:
#             # c=-1
#             print(b*b)
#         else:
#             # c=-1
#             print((c)*(c))
        
# (perfect_squre(5))
import math

# def perfect_square(t):
#     results = []
#     for _ in range(t):
#         num = int(input())
#         root = int(math.sqrt(num))
#         diff1 = num - root * root
#         b=root
#         diff2 = (b + 1) * (b + 1) - num
#         if diff2==0:
#             diff2 = (b + 2) * (b + 2) - num
#         if diff1 < diff2:
#             results.append( root * root)
#         else:
#             results.append((root + 1) * (root + 1))
#     return results

# t = int(input("Enter the number of test cases: "))
# output = perfect_square(t)
# print("Results:")
# for result in output:
#     print(result)

# import math
# def perfect_square(t):
#     a=[]
#     for i in range (t):
#         a.append(int(input()))
    
#     for n in a:
#         lower_square = int(math.floor(math.sqrt(n)) ** 2)
#         upper_square = int(math.ceil(math.sqrt(n)) ** 2)
        
#         if(lower_square == upper_square):
#             if((n-(math.sqrt(n)-1)**2) < ((math.sqrt(n)+1)**2 - n)):
#                 print(int((math.sqrt(n)-1)**2))
#             else:
#                 print(int((math.sqrt(n)+1)**2))
#         else:
#             if((n-lower_square) == ( upper_square - n)):
#                 print(int(upper_square))
#             elif abs(n - lower_square) < abs(n - upper_square):
#                 print(int(lower_square))
#             else:
#                 print(int(upper_square))
# perfect_square(int(input()))

# A Python 3 program to
# demonstrate working of
# recursion


# def printFun(test):

# 	if (test < 1):
# 		return
# 	else:

# 		# print(test, end=" ")
# 		printFun(test-1) # statement 2
# 		print(test, end=" ")
# 		return

# # Driver Code
# test = 3
# printFun(test)

# This code is contributed by
# Smitha Dinesh Semwal

def t(n):
    if n==4:
        return n
    else:
        return 2*t(n+1)
print(t(2))