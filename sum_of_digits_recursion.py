# def sum_of_digits(n, l=0):
#     if n == 0:
#         return l
#     return sum_of_digits(n // 10, l + n % 10)

# result = sum_of_digits(984)
# print(result)

def sum_of_digits(n):
    if n<10:
        return n
    return sum_of_digits(n // 10 )+ n % 10

result = sum_of_digits(984)
print(result)