from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.data = {}
        self.priority = OrderedDict()
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        ret = self.data[key]
        self.handler_priority(key)
        return ret

    def put(self, key: int, value: int) -> None:
        self.handler_priority(key)
        if key in self.data:
            self.data[key] = value
            return None
        if len(self.data) >= self.size:
            k = self.priority.popitem(False)[0]
            self.data.pop(k)
        self.data[key] = value

    def handler_priority(self, key):
        if key in self.priority:
            self.priority.move_to_end(key)
        else:
            self.priority[key] = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
