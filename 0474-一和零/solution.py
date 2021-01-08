class Solution:
    def __init__(self):
        self.cache = {}

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # count = self.dfs(strs, (0, m, n))
        count = self.solve(strs, m, n)
        return count

    def solve(self, strs, m, n):
        dp = []
        for _ in range(len(strs) + 1):
            tmp = [[0] * (n + 1) for _ in range(m + 1)]
            dp.append(tmp)
        for index in range(1, len(dp)):
            tmpM, tmpN = self.getCount(strs[index - 1])
            for i in range(len(dp[0])):
                for j in range(len(dp[0][0])):
                    if tmpM <= i and tmpN <= j:
                        dp[index][i][j] = max(
                            1 + dp[index-1][i-tmpM][j-tmpN], dp[index-1][i][j])
                    else:
                        dp[index][i][j] = dp[index-1][i][j]
        return dp[-1][-1][-1]

    def dfs(self, strs, info):
        index, m, n = info
        if index >= len(strs) or (m == 0 and n == 0):
            return 0
        if info in self.cache:
            return self.cache[info]
        count = 0
        for i in range(index, len(strs)):
            tmpM, tmpN = self.getCount(strs[i])
            if tmpM <= m and tmpN <= n:
                tmpInfo = (i + 1, m - tmpM, n - tmpN)
                tmp = self.dfs(strs, tmpInfo)
                count = max(count, 1 + tmp)
        self.cache[info] = count
        return count

    def getCount(self, s):
        m, n = 0, 0
        for c in s:
            if c == "0":
                m += 1
            else:
                n += 1
        return (m, n)
