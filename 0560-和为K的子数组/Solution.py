class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        helper = {0: 1}
        res, tmpsum = 0, 0
        for num in nums:
            tmpsum += num
            if (tmpsum - k) in helper:
                res += helper[tmpsum - k]
            helper[tmpsum] = helper.get(tmpsum, 0) + 1
        return res
