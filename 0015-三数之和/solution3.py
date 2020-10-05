class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                move_left, move_right = False, False
                if tmp == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    move_left, move_right = True, True
                elif tmp < 0:
                    move_left = True
                else:
                    move_right = True
                if move_left:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                if move_right:
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return ret

    
    """
        超时
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        nums.sort()
        self.dfs(nums, 0, [], ret)
        return ret

    def dfs(self, nums, index, path, ret):
        if len(path) == 3 and sum(path) == 0:
            ret.append(path)
            return None
        repeat = set()
        for i in range(index, len(nums)):
            if nums[i] in repeat:
                continue
            repeat.add(nums[i])
            self.dfs(nums, i+1, path+[nums[i]], ret)
        return None








