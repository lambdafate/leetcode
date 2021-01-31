class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        answer = []
        # init
        sums = [candiesCount[0]]
        for i in range(1, len(candiesCount)):
            sums.append(candiesCount[i] + sums[-1])
        for query in queries:
            all = 1
            if query[0] > 0: all += sums[query[0] - 1]
            days = query[1] + 1
            answer.append(query[1] < sums[query[0]] and query[2] * days >= all)
        return answer
