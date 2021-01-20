N = int(input())
matrix = []
for _ in range(N):
    matrix.append([float(n) for n in input().split()])

max_value = float("-inf")
indexs = None

def dfs(index, wait_used, path, value):
    global max_value, indexs
    if index >= N:
        flag = False
        if value > max_value:
            flag = True
        elif value == max_value:
            i = 0
            while i < N:
                if path[i] < indexs[i]:
                    flag = True
                    break
                i += 1
        if flag:
            max_value = value
            indexs = path
    for i in range(len(wait_used)):
        v = matrix[index][wait_used[i]]
        dfs(index + 1, wait_used[:i] + wait_used[i+1:], path + [wait_used[i]], value + v)

dfs(0, list(range(N)), [], 0)

print("%.2f"%max_value)
for i in range(N):
    print(f"{i + 1} {indexs[i] + 1}")