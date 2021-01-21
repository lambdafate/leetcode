import heapq

def readToInt():
    return [int(n) for n in input().split()]

NKM = readToInt()
graph = [set() for _ in range(NKM[0])]
for _ in range(NKM[2]):
    line = readToInt()
    v, u, w = line[0] - 1, line[1] - 1, line[2]
    graph[v].add((u, w))

def solve(graph, K):
    visisted = set()
    h = [(0, K)]
    ans = 0
    while len(h) != 0:
        time, v = heapq.heappop(h)
        if v in visisted:
            continue
        visisted.add(v)
        ans = time
        for u, w in graph[v]:
            if u not in visisted:
                heapq.heappush(h, (time + w, u))
    if len(visisted) == len(graph):
        return ans
    return -1

print(solve(graph, NKM[1] - 1))

