from bisect import bisect_left
from random import random
class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        target = self.total_sum * random()
        i = bisect_left(self.prefix_sums, target)
        return i
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

obj = Solution([1,3])

obj.pickIndex()