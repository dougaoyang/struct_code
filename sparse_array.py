def to_sparse_arr(arr):
    # TODO 校验二维数组的格式

    total_row = len(arr)
    total_col = len(arr[0])

    parse_arr = []
    parse_arr.append([total_row, total_col, 0])

    for i in range(total_row):
        for j in range(total_col):
            if arr[i][j]:
                parse_arr.append([i, j, arr[i][j]])
                parse_arr[0][2] += 1

    return parse_arr

def to_normal_arr(arr):
    # TODO 校验稀疏数组的格式

    normal_arr = []

    m = arr[0][0]
    n = arr[0][1]
    normal_arr = [[0] * m for i in range(n)]

    for item in arr[1:]:
        normal_arr[item[0]][item[1]] = item[2]
    
    return normal_arr

if __name__ == '__main__':
    # 初始化一个n*m的二维数组
    m = 10
    n = 10
    normal_arr = [[0] * m for i in range(n)]

    # 设置几个值
    normal_arr[1][2] = 1
    normal_arr[2][3] = 2
    normal_arr[4][5] = 2

    print('原始数组:\n{}'.format(normal_arr))

    sparse = to_sparse_arr(normal_arr)
    print('转化为稀疏数组:\n{}'.format(sparse))

    normal = to_normal_arr(sparse)
    print('转化为正常数组:\n{}'.format(normal))
