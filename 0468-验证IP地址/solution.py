class Solution:
    def validIPAddress(self, IP: str) -> str:
        flag = None
        target = {".", ":"}
        for c in IP:
            if c in target:
                flag = c
                break
        if flag == '.':
            if self.validIPv4(IP):
                return "IPv4"
        elif flag == ':':
            if self.validIPv6(IP):
                return "IPv6"
        return "Neither"
                
    def validIPv4(self, IP):
        nums = IP.split(".")
        if len(nums) != 4:
            return False
        for num in nums:
            if len(num) < 1 or len(num) > 3:
                return False
            if num[0] == '0' and len(num) > 1:
                return False
            if not num.isdigit():
                return False
            tmp = int(num)
            if tmp < 0 or tmp > 255:
                return False
        return True

    def validIPv6(self, IP):
        nums = IP.split(":")
        if len(nums) != 8:
            return False
        for num in nums:
            if len(num) < 1 or len(num) > 4:
                return False
            if not self.valid16(num):
                return False
        return True

    def valid16(self, num):
        for n in num:
            if n.isalpha():
                tmp = n.lower()
                if tmp < 'a' or tmp > 'f':
                    return False
        return True
