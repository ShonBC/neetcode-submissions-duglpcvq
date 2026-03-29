class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = OrderedDict() # {key : value}

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        self.lru.move_to_end(key)
        return self.lru[key]

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.move_to_end(key)
        self.lru[key] = value

        if len(self.lru) > self.capacity:
            self.lru.popitem(last=False)
