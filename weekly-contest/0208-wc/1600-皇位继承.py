class ThroneInheritance:
    def __init__(self, kingName):
        self.kingName = kingName
        self.orders = [[kingName, True, []]]
        self.cache = {kingName: 0}

    def birth(self, parentName, childName):
        index = self.cache[parentName]
        i = len(self.orders)
        self.cache[childName] = i
        self.orders.append([childName, True, []])
        self.orders[index][2].append(i)

    def death(self, name):
        index = self.cache[name]
        self.orders[index][1] = False

    def getInheritanceOrder(self):
        ret = []
        self.helper(0, ret)
        return ret
        
    def helper(self, i, ret):
        if self.orders[i][1]:
            ret.append(self.orders[i][0])
        for index in self.orders[i][2]:
            self.helper(index, ret)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance("king")
# obj.birth("king","childName")
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
# print(param_3)