def swap_case(char):
    if char.islower():
        return char.upper()

    elif char.isupper():
        return char.lower()
    return char

# Test cases
input1 = "hiHelloIndiaBihar"
temp = ""
i = 0
while(i<len(input1)):
    if (not input1[i].isupper()):
        temp += swap_case(input1[i])
    else:
        break
    i = i+1
print(temp)
temp = ""
while(i<len(input1)):
    if(input1[i].isupper() and len(temp)!=0):
        print(temp)
        temp = ""
        continue
    elif(input1[i].isupper()):
        temp += swap_case(input1[i])
    else:
        temp += swap_case(input1[i])
    i = i+1
    
print(temp)