class Solution:
    def twoSum(self, nums, target):
        helper = {}
        for index, value in enumerate(nums):
            if value in helper:
                return [helper[value], index]
            helper[target - value] = index
        return None


if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(Solution().twoSum(nums, target))