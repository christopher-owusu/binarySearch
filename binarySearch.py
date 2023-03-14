

def binarySearch(data, low, high, item):
    if low <= high:
        mid = (low + high) // 2
        if (data[mid] == item):
            return mid
        elif (item < data[mid]):
            return binarySearch(data, low, mid - 1, item)
        else:
            return binarySearch(data, mid + 1, high, item)
    else:
        return -1
    
num = [1,2,3,6,8,34,56]
print(binarySearch(num, 0, len(num) -1, 34))