# 计数排序

def count_sort(arr, start, end):
    count_arr = [0 for i in range(end-start+1)]

    # 遍历数组来填充计数数组
    for i in arr:
        count_arr[i] += 1

    # 对计数数组遍历求和
    for k, _ in enumerate(count_arr):
        if k:
            count_arr[k] = count_arr[k] + count_arr[k-1]

    # 填充排序数组
    sort_arr = [None for i in range(len(arr))]
    # 为了稳定性，倒序遍历
    for i in arr[::-1]:
        count_val = count_arr[i]
        sort_arr[count_val-1] = i
        count_arr[i] -= 1
        
    return sort_arr


# 计数排序 根据字典中的键来排序
def count_sort_dict(arr, key, start, end):
    count_arr = [0 for i in range(end-start+1)]

    # 遍历数组来填充计数数组
    for d in arr:
        count_arr[d[key]] += 1

    # 对计数数组遍历求和
    for k, _ in enumerate(count_arr):
        if k:
            count_arr[k] = count_arr[k] + count_arr[k-1]

    # 填充排序数组
    sort_arr = [None for i in range(len(arr))]
    # 为了稳定性，倒序遍历
    for d in arr[::-1]:
        count_val = count_arr[d[key]]
        sort_arr[count_val-1] = d
        count_arr[d[key]] -= 1

    return sort_arr


if __name__ == '__main__':
    # 假设考生成绩从0-5
    arr = [2, 5, 3, 0, 2, 3, 0, 3]
    print(arr)
    arr2 = count_sort(arr, 0, 5)
    print(arr2)
