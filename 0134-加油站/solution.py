class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        for i in range(len(gas)):
            # select a station to begin our maoxian
            allGas = 0
            j = i
            success = True
            for _ in range(len(gas)):
                allGas += gas[j] - cost[j]
                if allGas < 0:
                    success = False
                    break
                j = (j + 1) % len(gas)
            if success:
                return i
        return -1