# 选择排序

def select_sort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(i+1, l):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    arr = [10, 14, 6, 8, 32, 7, 3]
    print(select_sort(arr))

