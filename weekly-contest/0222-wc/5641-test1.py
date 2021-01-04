class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        count = 0
        i = 0
        while truckSize > 0 and i < len(boxTypes):
            box = boxTypes[i]
            tmp = min(box[0], truckSize)
            count += tmp * box[1]
            truckSize -= tmp
            i += 1
        return count
            