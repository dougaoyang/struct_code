# 快速排序
import random

# 获取分区点
def partition(arr, start, end):
    # i,j以此向后递推，i前面的都小于 下标p的值
    i, j = start, start
    # 获取分区点
    p = random.randint(start, end)
    while True:
        # 跳过下标p
        if i == p: i += 1
        if j == p: j += 1
        if j > end: break

        # 比较 j, p 将小于p的值交换到i的左侧
        if arr[j] < arr[p]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    if p < i:
        arr[i-1], arr[p] = arr[p], arr[i-1]
        r = i-1
    else:
        arr[i], arr[p] = arr[p], arr[i]
        r = i
    return r


def quick_sort(arr, start=0, end=None):
    end = len(arr) - 1 if end is None else end

    if start >= end:
        return

    r = partition(arr, start, end)
    quick_sort(arr, start, r-1)
    quick_sort(arr, r+1, end)


if __name__ == '__main__':
    arr = [10, 14, 6, 8, 32, 7, 3]
    print(arr)
    quick_sort(arr)
    print(arr)
