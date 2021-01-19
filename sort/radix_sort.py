# 基数排序
from count_sort import count_sort_dict


def radix_sort(arr):
    if len(arr) < 2:
        return arr

    # 获取数组中元素的长度
    item_len = len(arr[0])

    for cursor in range(item_len-1, -1, -1):
        tmp_arr = []
        for item in arr:
            tmp_arr.append({
                'sort': int(item[cursor]),
                'content': item,
            })
        tmp_arr = count_sort_dict(tmp_arr, 'sort', 0, 9)
        arr = [d['content'] for d in tmp_arr]

    return arr


if __name__ == '__main__':
    # 有一组手机号
    arr = [
        '15226868539',
        '14793796484',
        '15256719195',
        '16512609221',
        '13815352149',
        '18728617636',
        '18876615646',
        '18389322811',
        '19818862415',
        '15229013582',
    ]
    print(arr)
    arr2 = radix_sort(arr)
    print(arr2)
