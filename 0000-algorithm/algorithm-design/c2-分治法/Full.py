"""
    螺旋矩阵
"""


def full(size):
    res = [[0]*size for _ in range(size)]
    num = 1

    def helper(size, i, j):
        nonlocal res
        nonlocal num
        if size <= 0:
            return None
        if size == 1:
            res[i][j], num = num, num+1
            return None
        for row in range(i, size+i-1):
            res[row][j], num = num, num+1
        for clo in range(j, size+j-1):
            res[size+i-1][clo], num = num, num+1
        for row in range(size+i-1, i, -1):
            res[row][size+j-1], num = num, num+1
        for clo in range(size+j-1, j, -1):
            res[i][clo], num = num, num+1
        helper(size-2, i+1, j+1)

    helper(size, 0, 0)
    return res


if __name__ == "__main__":
    res = full(4)
    for line in res:
        print(line)