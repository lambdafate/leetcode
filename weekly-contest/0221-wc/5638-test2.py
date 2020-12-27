import heapq

class Solution:
    def eatenApples(self, apples, days):
        count = 0
        i = 0
        h = []
        while i < len(apples):
            if apples[i] != 0:
                heapq.heappush(h, (i + days[i], apples[i]))
            while h and (h[0][0] <= i or h[0][1] <= 0):
                heapq.heappop(h)
            if len(h) != 0:
                apple = heapq.heappop(h)
                count += 1
                # print(f"{i} -- {apple}")
                if apple[1] > 1:
                    heapq.heappush(h, (apple[0], apple[1] - 1))
            i += 1
        while h:
            if h[0][0] <= i or h[0][1] <= 0:
                heapq.heappop(h)
                continue
            apple = heapq.heappop(h)
            size = min(apple[1], apple[0] - i)
            count += size
            i += size
        return count

if __name__ == "__main__":
    a = [1, 2, 3, 5, 2]
    d = [3, 2, 1, 4, 2]
    ret = Solution().eatenApples(a, d)
    print(ret)
