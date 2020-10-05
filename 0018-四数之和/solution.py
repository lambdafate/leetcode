class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left, right = j+1, len(nums)-1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    move_left, move_right = False, False
                    if tmp == target:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        move_left, move_right = True, True
                    elif tmp < target:
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
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        ret = []
        nums.sort()
        self.dfs(nums, 0, target, [], ret)
        return ret

    def dfs(self, nums, index, target, path, ret):
        if len(path) == 4 and target == 0:
            ret.append(path)
            return None        
        repeat = set()
        for i in range(index, len(nums)):
            if nums[i] in repeat:
                continue
            repeat.add(nums[i])
            self.dfs(nums, i+1, target-nums[i], path+[nums[i]], ret)
        return None
