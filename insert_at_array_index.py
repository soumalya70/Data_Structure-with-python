def insertAtIndex(self, arr, sizeOfArray, index, element):
    #Your code here
    # i=index
    if index < 0 or index > sizeOfArray:
        return -1
            
    arr.append(None)
    for i in range(sizeOfArray,index,-1):
        arr[i] = arr[i-1]
    arr[index] = element
    return arr

        