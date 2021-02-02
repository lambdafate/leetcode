class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        left, right = 0, 0
        maxCount = 0
        counts = [0] * 26
        index = lambda c: ord(c) - ord('A')
        while right < len(s):
            i = index(s[right])
            counts[i] += 1
            maxCount = max(maxCount, counts[i])
            window = right - left + 1
            if window - maxCount > k:
                counts[index(s[left])] -= 1
                left += 1
            right += 1
        return right - left


if __name__ == "__main__":
    s = "BAAAB"
    k = 2
    ans = Solution().characterReplacement(s, k)
    print(ans)
