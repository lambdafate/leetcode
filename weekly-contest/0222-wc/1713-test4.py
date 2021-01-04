class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        maps = {}
        for i, n in enumerate(target):
            maps[n] = i
        arrays = [n for n in arr if n in maps]
        dp = [1] * len(arrays)
        for i in range(1, len(dp)):
            for j in range(i-1, -1, -1):
                if maps[arrays[j]] < maps[arrays[i]]:
                    dp[i] = max(dp[i], dp[j] + 1)
                elif maps[arrays[j]] == maps[arrays[i]]:
                    dp[i] = max(dp[i], dp[j])
                    break
        return len(target) - max(dp)
