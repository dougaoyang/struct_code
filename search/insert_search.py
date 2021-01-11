# 插入排序

def insert_search(arr):
    l = len(arr)
    for i in range(1, l):
        val = arr[i]
        # 查找插入的位置
        j = i - 1
        while j >= 0:
            # 如果前面的有序集中有数大于比较的数，则以此向后移动一位
            if arr[j] > val:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break
        arr[j+1] = val
    return arr


if __name__ == '__main__':
    arr = [10, 14, 6, 8, 32, 7, 3]
    print(insert_search(arr))


