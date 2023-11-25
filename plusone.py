
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    new_digits = [0] * (len(digits) + 1)
    new_digits[0] = 1
    return new_digits
print(plusOne([2,3,9,7]))
# num=[5,2,3,4]
# digits=[0]*(len(num) + 1)
# digits[0]=1
# print(digits)