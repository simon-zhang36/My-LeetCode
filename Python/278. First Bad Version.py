# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(x):
    return x >= FIRST_BAD

class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1
        if left >= n+1 or not isBadVersion(left):
            return -1
        return left


FIRST_BAD = 1
s = Solution()
s.firstBadVersion(0)