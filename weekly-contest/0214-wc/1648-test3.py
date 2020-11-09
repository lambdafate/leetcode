class Solution:
    """
        TLE
    """
    def maxProfit(self, inventory, orders):
        if not inventory or orders <= 0:
            return 0
        if len(inventory) == 1:
            ret = ((inventory[0] - orders + 1 + inventory[0])) * orders // 2
            return ret % (10**9 + 7)
        inventory.sort(reverse=True)
        ret = 0
        for _ in range(orders):
            if inventory[0] <= 0:
                return 0
            ret += inventory[0]
            ret = ret % (10 ** 9 + 7)
            inventory[0] -= 1
            # inventory.sort(reverse=True)
            i = 0
            while i < len(inventory) - 1:
                if inventory[i] < inventory[i+1]:
                    inventory[i], inventory[i+1] = inventory[i+1], inventory[i]
                else:
                    break
                i += 1
        return ret % (10**9 + 7)
