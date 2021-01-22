class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        curr = n % 10
        high = n // 10
        count = 0
        low = 0
        ans = 0
        while high != 0 or curr != 0:
            if curr == 0:
                ans += high * 10**count
            elif curr == 1:
                ans += high * 10**count + low + 1
            else:
                ans += (high + 1) * 10**count
            low = curr * 10**count + low
            count += 1
            curr = high % 10
            high = high // 10
        return ans


if __name__ == "__main__":
    Solution().countDigitOne(12)