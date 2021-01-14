# 归并排序

def merge_sort(arr, start=0, end=None):
    end = len(arr) - 1 if end is None else end
    if start >= end:
        return [arr[start]]

    mid = (start + end) // 2

    l_arr = merge_sort(arr, start, mid)
    r_arr = merge_sort(arr, mid+1, end)

    # 合并左右数组
    tmp, i, j = [], 0, 0
    while i <= len(l_arr) - 1 and j <= len(r_arr) - 1:
        # 取最小的放入临时数组
        if l_arr[i] <= r_arr[j]:
            tmp.append(l_arr[i])
            i += 1
        else:
            tmp.append(r_arr[j])
            j += 1
    # 将剩余的元素放进临时数组中
    for k in l_arr[i:]:
        tmp.append(k)
    for k in r_arr[j:]:
        tmp.append(k)
    return tmp

if __name__ == '__main__':
    arr = [10, 14, 6, 8, 32, 7, 3]
    print(merge_sort(arr))

