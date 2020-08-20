class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        num = 0
        for n in nums:
            num ^= n
        index = 0
        while (num & 1) == 0:
            num = num >> 1
            index += 1
        flag = 1 << index
        r1, r2 = 0, 0
        for n in nums:
            if flag & n == 0:
                r1 ^= n
            else:
                r2 ^=n
        return [r1, r2]