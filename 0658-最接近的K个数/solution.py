class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        i, j = 0, len(arr)-1
        while i < j-1:
            mid = (i + j) // 2
            if arr[mid] == x:
                i, j = mid, mid
                break
            elif arr[mid] < x:
                i = mid
            else:
                j = mid
        if i != j:
            if abs(arr[i]-x) <= abs(arr[j]-x):
                j = i
            else:
                i = j
        for _ in range(k-1):
            if i == 0 or j == len(arr)-1:
                break
            if abs(arr[i-1]-x) <= abs(arr[j+1]-x):
                i -= 1
            else:
                j += 1
        if i == 0:
            j = i + k -1
        elif j == len(arr) -1:
            i = len(arr) - k
        return arr[i:j+1]
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda item: (abs(item-x), item))
        ret = arr[:k]
        ret.sort()
        return ret
