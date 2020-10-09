class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust is None:
            return -1
        # 入度
        data1 = [0] * N
        # 出度
        data2 = [0] * N
        for t in trust:
            data2[t[0]-1] += 1
            data1[t[1]-1] += 1
        for i in range(N):
            if data1[i] == N-1 and data2[i] == 0:
                return i+1
        return -1
    
    
    
    
    
    """
        邻接表
    """
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust is None:
            return -1
        grid = [set() for _ in range(N)]
        for t in trust:
            grid[t[0]-1].add(t[1]-1)
        for i in range(len(grid)):
            if self.checkJudge(grid, i):
                return i+1
        return -1

    def checkJudge(self, grid, index):
        if len(grid[index]) != 0:
            return False
        for i in range(len(grid)):
            if i != index and index not in grid[i]:
                return False
        return True







    """
        邻接矩阵
    """
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if trust is None:
            return N
        grid = [[False] * N for _ in range(N)]
        for t in trust:
            grid[t[0]-1][t[1]-1] = True
        for person in range(len(grid)):
            if self.checkJudge(grid, person):
                return person + 1
        return -1

    def checkJudge(self, grid, index):
        for trust in grid[index]:
            if trust:
                return False
        for i in range(len(grid)):
            if i != index and not grid[i][index]:
                return False
        return True
                