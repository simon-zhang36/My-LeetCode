from typing import List
import bisect
from collections import defaultdict

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._tree_map = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._tree_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        k = self._tree_map.get(key)
        if not k:
            return ""
        i = bisect.bisect_right(k, (timestamp, chr(127)))
        return k[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)