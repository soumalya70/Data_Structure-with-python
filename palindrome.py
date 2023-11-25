def isPalindrome(n):
    rev=0
    temp=n
    while temp!=0:
        a=temp%10
        rev=rev*10+a
        temp=temp//10
    return rev==n

print(isPalindrome(7909))