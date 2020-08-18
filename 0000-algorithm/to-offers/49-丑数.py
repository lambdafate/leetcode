class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l2, l3, l5 = [2], [3], [5]
        curr = 1
        for _ in range(n-1):
            curr = min(l2[0], l3[0], l5[0])
            if curr == l2[0]:
                l2.pop(0)
            if curr == l3[0]:
                l3.pop(0)
            if curr == l5[0]:
                l5.pop(0)
            l2.append(2 * curr)
            l3.append(3 * curr)
            l5.append(5 * curr)
        return curr
        
