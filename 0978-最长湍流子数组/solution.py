class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        bools = []
        for i in range(1, len(arr)):
            bools.append(arr[i-1] - arr[i])
        dp = [0] * len(bools)
        if bools[0] != 0:
            dp[0] = 1
        for i in range(1, len(dp)):
            if (bools[i] > 0 and bools[i-1] < 0) or (bools[i] < 0 and bools[i-1] > 0):
                dp[i] = 1 + dp[i-1]
            elif bools[i] == 0:
                dp[i] = 0
            else:
                dp[i] = 1
        # print(bools)
        # print(dp)
        return max(dp) + 1
