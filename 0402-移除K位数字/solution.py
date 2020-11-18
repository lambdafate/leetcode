class Solution:
    """
        贪心 + 单调栈
    """
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or len(num) == 0 or k <= 0 or k > len(num):
            return num
        stack = []
        index = 0
        while True:
            while k > 0 and stack and stack[-1] > num[index]:
                k -= 1
                stack.pop()
            if k == 0:
                break
            while index < len(num) - 1 and num[index] <= num[index+1]:
                stack.append(num[index])
                index += 1
            if index < len(num) - 1:
                # delete num[index]
                # print(num[index])
                k -= 1
                index += 1
            else:
                break
        ret = "".join(stack) + num[index:]
        if k > 0:
            ret = ret[:len(ret) - k]
        if ret:
            ret = str(int(ret))
        else:
            ret = "0"
        return ret
        


    """
    # 贪心 pass 5% :)
    # k == len(num) --> "0"
    # '0200'  --> '200' 结果要去掉前缀0
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or len(num) == 0 or k <= 0 or k > len(num):
            return num
        nums = list(num)
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i+1]:
            i += 1
        ret = None
        if i >= len(nums) - 1:
            ret = num[:len(num) - k]
        else:
            nums[i] = ""
            ret = self.removeKdigits("".join(nums), k - 1)
        if ret:
            ret = str(int(ret))
        else:
            ret = "0"
        return ret
    """


    """
    # 由 dfs+记忆化 推导出 dp, pass 22/33
    def removeKdigits(self, num: str, k: int) -> str:
        if not num or len(num) == 0 or k <= 0:
            return num
        # dp[i][j] = min(dp[i][j-1] * 10 + num[j],  dp[i-1][j-1])
        dp = [[0] * len(num) for _ in range(k + 1)]
        # init
        n = 0
        for j in range(len(dp[0])):
            n = n * 10 + int(num[j])
            dp[0][j] = n
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1] * 10 + int(num[j]))
        return str(dp[k][-1])
    """


if __name__ == "__main__":
    ret = Solution().removeKdigits("1234567890", 9)
    print(ret)