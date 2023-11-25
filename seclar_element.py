# def lar(l):
#     res=l[0]
#     for i in range(1,len(l)):
#         if l[i]>res:
#             res=l[i]
#     return res
# # print(lar([2,8,5,6,1]))

# def slar(l):
#     if len(l)<=1:
#         return None
#     m=lar(l)
#     slar=None
#     for x in l:
#         if x!=m:
#             if slar==None:
#                 slar=x
#             else:
#                 slar=max(x,slar)
#     return slar
def selar(l):
    if len(l)<=1:
        return None
    lar=l[0]
    slar=None
    for x in l[1:]:
        if x>lar:
            slar=lar
            lar=x
        elif x!=lar:
            if slar==None or slar<x:
                slar=x
    return slar
l=[int(x) for x in input().split()]
print(selar(l))
    
    