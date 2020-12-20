class Solution:
    def reformatNumber(self, number: str) -> str:
        nums = [n for n in number if n.isdigit()]
        nums = "".join(nums)
        ret = []
        i = 0
        # print(nums)
        while i < len(nums):
            size = len(nums) - i
            if size == 4:
                ret.append(nums[i] + nums[i+1])
                ret.append(nums[i+2] + nums[i+3])
                i += 4
                continue
            length = 3
            if size == 2:
                length = 2
            ret.append(nums[i:i+length])
            i += length
        return "-".join(ret)
