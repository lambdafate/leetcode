class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ways = 0
        # init
        prevOdd, prevEven = 0, 0
        leftOdd, leftEven = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                leftEven += nums[i]
            else:
                leftOdd += nums[i]

        for i in range(len(nums)):
            # delete i
            odd, even = prevOdd, prevEven
            tmpOdd, tmpEven = leftOdd, leftEven
            if i % 2 == 0:
                tmpEven -= nums[i]
            else:
                tmpOdd -= nums[i]
            odd += tmpEven
            even += tmpOdd
            # count ways
            if odd == even:
                ways += 1
            # update
            if i % 2 == 0:
                prevEven += nums[i]
                leftEven -= nums[i]
            else:
                prevOdd += nums[i]
                leftOdd -= nums[i]
        return ways