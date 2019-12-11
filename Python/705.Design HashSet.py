class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i,j in enumerate(bucket):
            if key == j:
                return bucket, j
        return bucket, -1


    def add(self, key: int) -> None:
        bucket, idx = self._index(key)
        if idx == -1: bucket.append(key)

    def remove(self, key: int) -> None:
        bucket, idx = self._index(key)
        if idx >=0: bucket.remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        bucket, idx = self._index(key)
        return idx >= 0
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)