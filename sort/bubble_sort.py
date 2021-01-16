# 冒泡排序

def bubble_sort(arr):
    l = len(arr)
    for i in range(l):
        flag = 0 # 判断一轮中有没有比较过
        for j in range(0, l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1  # 表示有数据交换
        if not flag: break


if __name__ == '__main__':
    arr = [10, 14, 6, 8, 32, 7, 3]
    print(arr)
    bubble_sort(arr)
    print(arr)
