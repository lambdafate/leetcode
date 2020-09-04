class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        v = self.cache.get(key, -1)
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)
        return v

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and len(self.cache) >= self.capacity:
            k = self.queue.pop(0)
            del self.cache[k]
        if key in self.cache:
            self.queue.remove(key)
        self.queue.append(key)
        self.cache[key] = value


"""
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.access = {}
        self.capacity = capacity
        self.ticks = 0

    def get(self, key: int) -> int:
        v = self.cache.get(key, -1)
        if key in self.cache:
            self.access[key] = self.ticks
        self.ticks += 1
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.access[key] = self.ticks
            self.ticks += 1
            return
        if len(self.cache) >= self.capacity:
            # 要淘汰一个数据
            destory_key, destory_access = -1, self.ticks
            for k, v in self.access.items():
                if v < destory_access:
                    destory_key, destory_access = k, v
            del self.cache[destory_key]
            del self.access[destory_key]
        self.cache[key] = value
        self.access[key] = self.ticks
        self.ticks += 1
"""



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
