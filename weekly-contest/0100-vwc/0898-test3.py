class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        if not A:
            return 0
        cache = set()
        dp = [[0] * len(A) for _ in range(len(A))]
        for i in range(len(dp)-1, -1, -1):
            for j in range(i, len(dp)):
                if i == j:
                    dp[i][j] = A[i]
                elif i == j - 1:
                    dp[i][j] = A[i] | A[j]
                else:
                    dp[i][j] = A[i] | A[j] | dp[i+1][j-1]
                cache.add(dp[i][j])
        return len(cache)