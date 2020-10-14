class Solution:
    def __init__(self):
        self.sp = {
            4: "IV", 9: "IX",
            40: "XL", 90: "XC",
            400: "CD", 900: "CM"
        }
        self.mapper = [
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]
    
    def intToRoman(self, num: int) -> str:
        ret = []
        nums = list(str(num))
        i = 0
        while num != 0 and i < len(nums):
            n = int(nums[i]) * 10**(len(nums)-i-1)
            num -= n
            if n != 0:
                ret.append(self.convert(n))
            i += 1
        return "".join(ret)
    
    def convert(self, num):
        if num <= 0:
            return ""
        if num in self.sp:
            return self.sp[num]
        index = 0
        for i in range(len(self.mapper)-1, -1, -1):
            if self.mapper[i][1] <= num:
                index = i
                break
        times = num // self.mapper[index][1]
        num = num % self.mapper[index][1]
        ret = self.mapper[index][0] * times
        if num != 0:
            ret += self.convert(num)
        return ret

if __name__ == "__main__":
    ret = Solution().intToRoman(58)
    print(ret)