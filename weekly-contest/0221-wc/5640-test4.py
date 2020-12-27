class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        nums = list(set(nums))
        nums.sort()
        for query in queries:
            x, m = query[0], query[1]
            tmp = float("-inf")
            for n in nums:
                if n > m:
                    break
                tmp = max(tmp, x ^ n)
            if tmp == float("-inf"):
                tmp = -1
            ans.append(tmp)
        return ans
