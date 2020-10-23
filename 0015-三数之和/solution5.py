class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        index = 0
        while index <= len(nums)-3:
            if index > 0 and nums[index] == nums[index-1]:
                index += 1
                continue
            i, j = index+1, len(nums)-1
            while i < j:
                tmp = nums[index] + nums[i] + nums[j]
                move_i, move_j = False, False
                if tmp == 0:
                    ret.append([nums[index], nums[i], nums[j]])
                    move_i, move_j = True, True
                elif tmp < 0:
                    move_i = True
                else:
                    move_j = True
                if move_i:
                    tmp = i
                    while tmp < j and nums[tmp] == nums[i]:
                        tmp += 1
                    i = tmp
                if move_j:
                    tmp = j
                    while tmp > i and nums[tmp] == nums[j]:
                        tmp -= 1            
                    j = tmp
            index += 1
        return ret

    """
        dfs -> tle
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        self.dfs(nums, 0, 0, [], ret)
        return ret

    def dfs(self, nums, index, target, path, ret):
        if len(path) == 3:
            if target == 0:
                ret.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            if i != index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, target-nums[i], path+[nums[i]], ret)
        