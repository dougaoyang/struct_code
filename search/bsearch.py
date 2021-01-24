import math

# 二分查找

def bsearch(arr, val):
    def _bsearch(arr, low, heigh, val):
        if low > heigh:
            return -1
        
        mid = math.ceil((low + heigh) / 2)
        if val == arr[mid]:
            return mid
        elif val > arr[mid]:
            return _bsearch(arr, mid+1, heigh, val)
        else:
            return _bsearch(arr, low, mid-1, val)

    return _bsearch(arr, 0, len(arr)-1, val)


if __name__ == '__main__':
    arr = [8, 11, 19, 23, 27, 33, 45, 55, 67, 98]
    print(bsearch(arr, 98))
