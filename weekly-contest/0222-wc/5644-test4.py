from typing import *

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dp = [[0] * len(target) for _ in range(len(arr))]
        flag = False
        for j in range(len(dp[0])):
            if not flag and arr[0] == target[j]:
                flag = True
            if flag: dp[0][j] = j
            else: dp[0][j] = j + 1
        flag = False
        for i in range(len(dp)):
            if arr[i] == target[0]: break
            dp[i][0] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if arr[i] == target[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(1 + dp[i][j-1], dp[i-1][j])
        # for line in dp:
        #     print(line)
        return dp[-1][-1]


if __name__ == "__main__":
    ret = Solution().minOperations(
[147006006, 414087855, 781906580, 213872647, 341866400, 674590438, 530308968, 178008557, 87329397, 886710682],
[530308968, 147006006, 672718815, 341866400, 886710682, 341866400, 530308968, 178008557, 6513508, 6513508])
    print(ret)
