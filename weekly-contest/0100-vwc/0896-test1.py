class Solution:
    def isMonotonic(self, A):
        if not A or len(A) < 2:
            return True
        i = 1
        while i < len(A) and A[i] == A[i-1]:
            i += 1
        if i >= len(A):
            return True
        mons = A[i-1] < A[i]
        for j in range(i, len(A)):
            if mons and A[j] < A[j-1]:
                return False
            if not mons and A[j] > A[j-1]:
                return False
        return True


if __name__ == "__main__":
    ret = Solution().isMonotonic([1, 3, 2])
    print(ret)