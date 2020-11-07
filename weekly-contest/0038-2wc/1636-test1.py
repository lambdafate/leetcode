class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cache = {}
        for num in nums:
            if num not in cache:
                cache[num] = 0
            cache[num] += 1
        nums.sort(key=lambda item: (cache[item], -item))
        return nums
