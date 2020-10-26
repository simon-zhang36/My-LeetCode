from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Binary Search
        You may imagine that nums[-1] = nums[n] = -∞
        so -∞ [x, y, z] -∞ will always have a peak
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()

s.findPeakElement([1])
s.findPeakElement([1,2,3,1])
s.findPeakElement([1,2,1,3,5,6,4])
s.findPeakElement([1,2,1])
s.findPeakElement([3,2,1])
s.findPeakElement([1,2,3])