class MyHashMap:

    # todo
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hs = self._hash(key)
        bucket = self.buckets[hs]
        if not bucket:
            return hs, -1
        else:
            for idx, item in enumerate(bucket):
                if key == item[0]:
                    return hs, idx
            return hs, -1

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hs, idx = self._index(key)
        if idx == -1:
            self.buckets[hs].append([key, value])
        else:
            self.buckets[hs][idx][1] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hs, idx = self._index(key)
        if idx == -1:
            return -1
        else:
            return self.buckets[hs][idx][1]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash, idx = self._index(key)
        if idx != -1:
            del self.buckets[hash][idx]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(1, 2)
# param_2 = obj.get(1)
# param_2
# obj.remove(1)
