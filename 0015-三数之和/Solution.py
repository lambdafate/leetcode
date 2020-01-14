class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        i, j, k = 0, 1, 2
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        norepeat = []
        for i in res:
            isrepeat = False
            for j in norepeat:
                first, second = sorted(i), sorted(j)
                if first[0] == second[0] and first[1] == second[1]:
                    isrepeat = True
                    break
            if isrepeat:
                continue
            norepeat.append(i)
        
        return norepeat


if __name__ == "__main__":
    print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

