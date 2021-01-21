def readToInt():
    return [int(n) for n in input().split()]

companyA = readToInt()
companyB = readToInt()
pairs = []
for _ in range(int(input())):
    pairs.append(readToInt())

count = float("inf")

def dfs(index, selected):
    global count
    if index >= len(pairs):
        count = min(count, len(selected))
        return
    if len(selected) >= count:
        return
    pair = pairs[index]
    if pair[0] in selected or pair[1] in selected:
        dfs(index + 1, selected)
    else:
        selected.add(pair[0])
        dfs(index + 1, selected)
        selected.remove(pair[0])
        selected.add(pair[1])
        dfs(index + 1, selected)
        selected.remove(pair[1])

dfs(0, set())
print(count)