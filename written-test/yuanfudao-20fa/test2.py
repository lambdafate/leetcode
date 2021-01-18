def readToInt():
    return [int(n) for n in input().split()]

max_steps = 0
line = readToInt()
K = line[2]
matrix = []
positions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

def dfs(i, j, steps, k):
    global max_steps
    max_steps = max(max_steps, steps)
    for p in positions:
        x, y = i + p[0], j + p[1]
        if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
            continue
        if matrix[i][j] < matrix[x][y]:
            dfs(x, y, steps + 1, k)
        if k > 0:
            dfs(x, y, steps + 1, k - 1)
    return

for _ in range(line[0]):
    matrix.append(readToInt())
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        dfs(i, j, 1, K)
print(max_steps)
