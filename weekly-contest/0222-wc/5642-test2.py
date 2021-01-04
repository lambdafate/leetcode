class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        maps = {}
        for n in deliciousness:
            if n not in maps:
                maps[n] = 1
            else:
                maps[n] += 1
        ret = 0
        for num in maps:
            n = 1
            for _ in range(24):
                k = n - num
                if k in maps:
                    if k != num:
                        ret += maps[k] * maps[num]
                    elif maps[k] > 1:
                        ret += maps[k] * (maps[k] - 1)
                n = n << 1
        return (ret // 2) % (10**9 + 7)

