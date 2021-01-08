class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = [set() for _ in range(n)]
        for flight in flights:
            graph[flight[0]].add((flight[1], flight[2]))
        price = float("inf")

        def dfs(src, dst, money, k):
            nonlocal price
            if src == dst:
                price = min(price, money)
                return
            # 这里增加 money > price 的判断条件, 就可以AC
            if k < 0 or money > price:
                return
            for nbs in graph[src]:
                dfs(nbs[0], dst, money + nbs[1], k - 1)
        dfs(src, dst, 0, K)
        if price == float("inf"):
            return -1
        return price
