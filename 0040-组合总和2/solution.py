class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        ret = []
        self.dfs(candidates, 0, target, [], ret)
        return ret

    def dfs(self, nums, index, target, path, ret):
        if target == 0:
            ret.append(path)
        repeat = set()
        for i in range(index, len(nums)):
            if target < nums[i]:
                break
            if nums[i] in repeat:
                continue
            repeat.add(nums[i])            
            self.dfs(nums, i+1, target-nums[i], path+[nums[i]], ret)