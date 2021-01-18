# 桶排序
from quick_sort import quick_sort
from collections import defaultdict
import math


def bucket_sort(arr, start, end, m):
    """
    桶排序
    @param arr   待排序数组
    @param start 取值范围
    @param end   取值范围
    @param m   需要分成几个桶
    """
    # 分成m个桶
    buckets = [[] for i in range(m)]

    interval = (end - start) // m
    for i in arr:
        bucket_idx = math.floor(i / interval)
        bucket_idx = min(bucket_idx, m)
        buckets[bucket_idx].append(i)

    data = []
    for bucket in buckets:
        quick_sort(bucket) # 每个桶里的元素使用快排
        data = [*data, *bucket]
    return data

if __name__ == '__main__':
    # 假设有一组订单在0-50的订单
    arr = [22,5,11,41,45,26,29,10,7,8,30,27,42,43,40]
    print(arr)
    arr2 = bucket_sort(arr, 0, 50, 6)
    print(arr2)


