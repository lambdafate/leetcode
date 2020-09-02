class Solution:
    """
        将列表根据身高降序排列，之后根据K值插入到输出队列
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (-p[0], p[1]))
        ret = []
        for p in people:
            ret.insert(p[1], p)
        return ret
