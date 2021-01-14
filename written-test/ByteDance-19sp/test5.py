def readToInt():
    return [int(n) for n in input().split()]

def solve(graph):
    dp = [[float("inf")] * (len(graph) - 1) for _ in range(2**(len(graph) - 1))]
    for j in range(len(dp[0])):
        dp[0][j] = graph[j + 1][0]
    for i in range(1, len(dp)):
        indexs = []
        bits, index = i, 0
        while bits:
            if bits & 1 == 1:
                indexs.append(index)
            bits = bits >> 1
            index += 1
        for j in range(len(dp[0])):
            for index in indexs:
                dp[i][j] = min(dp[i][j], graph[j + 1][index + 1] + dp[i & ~(1 << index)][index])
    prices = float("inf")
    for j in range(1, len(graph)):
        prices = min(prices, graph[0][j] + dp[-1][j - 1])
    return prices

if __name__ == "__main__":
    graph = []
    for _ in range(int(input())):
        graph.append(readToInt())
    if len(graph) <= 1:
        print(0)
    else:
        print(solve(graph))
