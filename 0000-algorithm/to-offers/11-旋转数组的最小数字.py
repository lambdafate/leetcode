class Solution:
    # 更简洁的二分查找
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers)-1
        while i < j:
            mid = (i + j) // 2
            if numbers[mid] < numbers[j]:
                j = mid
            elif numbers[mid] > numbers[j]:
                i = mid + 1
            else:
                j -= 1
        return numbers[i]

    """
    # 二分查找
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers)-1
        while i < j and numbers[i] == numbers[i+1]:
            i += 1
        while i < j and numbers[j] == numbers[j-1]:
            j -= 1
        while i < j:
            mid = (i + j) // 2
            if numbers[mid] <= numbers[j]:
                j = mid
            else:
                i = mid + 1
        if i == j:
            return numbers[i]
        return numbers[0]
    """

    """
    # 一趟遍历
    def minArray(self, numbers: List[int]) -> int:
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[i-1]:
                return numbers[i]
        return numbers[0]
    """
