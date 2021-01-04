class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        sums = [0]
        allSum = nums[0]
        for i in range(1, len(nums)):
            sums.append(sums[i-1] + nums[i-1])
            allSum += nums[i]
        count = 0
        for i in range(1, len(nums) - 1):
            if sums[i] * 3 > allSum:
                break
            j0 = self.getLowBound(sums, i + 1, sums[i] * 2)
            j1 = self.getHighBound(
                sums, i + 1, ((allSum - sums[i]) // 2) + sums[i])
            count += max(0, j1 - j0 + 1)
        return count % (10**9 + 7)

    def getLowBound(self, nums, index, target):
        i, j = index, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        return i

    def getHighBound(self, nums, index, target):
        i, j = index, len(nums) - 1
        while i < j:
            mid = i + (j - i) // 2
            if i == j - 1:
                if nums[j] <= target:
                    return j
                return i
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        return i
