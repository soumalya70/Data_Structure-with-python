# def large(l):
#     for x in l:
#         for y in l:
#             if y>x:
#                 break
#         else:
#             return x
#     return None
def large(l):
    res=l[0]
    if not l:
        return None
    else:
        for i in range(1,len(l)):
            if l[i]>res:
                res=l[i-1]
                m=l[i-1]
        return m

print(large([5,6,1,7,8,9,41,40]))