class MaxHeap(object):
    def __init__(self):
        self.heap = [0]
    
    def insert(self, item):
        self.heap.append(item)
        self.swim(len(self.heap)-1)

    def getMax(self):
        if len(self.heap) <= 1:
            return None
        ret = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.sink(1)
        return ret

    """ 
        下沉
    """
    def sink(self, i):
        index = len(self.heap) - 1
        while i*2 <= index:
            j = i * 2
            if j + 1 <= index and self.heap[j] < self.heap[j+1]:
                j += 1
            if self.heap[j] <= self.heap[i]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
        return None

    """
        上升
    """
    def swim(self, i):
        while i > 1:
            j = i // 2
            if self.heap[j] >= self.heap[i]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j
        return None


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = MaxHeap()
        for num in nums:
            maxheap.insert(num)
        ret = None
        for _ in range(k):
            ret = maxheap.getMax()
        return ret