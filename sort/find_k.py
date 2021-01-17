from quick_sort import partition


def find_k(arr, k):
    start = 0
    end = len(arr) - 1
    if end < 2:
        return None

    # 目标下标
    dist = len(arr) - k
    r = None
    while dist != r:
        r = partition(arr, start, end)
        if r > dist:
            end = r - 1
        elif r < dist:
            start = r + 1

    return arr[r]
    

if __name__ == '__main__':

    arr = [10, 14, 6, 8, 32, 7, 3, 6, 8, 9]
    print(arr)
    # quick_sort(arr)
    print(find_k(arr, 3))
    print(arr)





