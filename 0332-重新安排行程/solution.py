"""
    几个坑:
        1. A -> B 的票可能不止一张
        2. 如果把所有可能行程遍历出来会超时
"""

class Solution:
    def __init__(self):
        self.paths = None

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 初始化邻接表
        graph = {}
        for ticket in tickets:
            if ticket[0] not in graph:
                # ticket status:
                # 0: 未使用
                # 1: 已使用
                graph[ticket[0]] = [[ticket[1], 0]]
            else:
                graph[ticket[0]].append([ticket[1], 0])
        # 如果有票 A->B/C/D, 对B/C/D进行排序, 遍历时从字典序较小的开始
        # 如果先到B是一种"行程", 那么该行程即为最终答案, 因为到C/D的行程字典序肯定大
        for k in graph:
            graph[k].sort(key=lambda x: x[0])
            # print(f"{k} -- {graph[k]}")
        self.dfs(graph, "JFK", [], len(tickets))
        return self.paths

    def dfs(self, graph, addr, path, ticketNum):
        path.append(addr)
        # 每张票必须用一次, 全部用完则结束搜索
        if ticketNum <= 0:            
            self.paths = path
            return
        # 构建的图不是真正的邻接表, 如果addr没有后续地点, 则addr不会在graph中 
        if addr not in graph:
            return
        for ticket in graph[addr]:
            if ticket[1] == 0:
                # 将票的状态设为已使用
                ticket[1] = 1
                self.dfs(graph, ticket[0], path.copy(), ticketNum - 1)
                # check self.paths
                if self.paths:
                    return
                ticket[1] = 0