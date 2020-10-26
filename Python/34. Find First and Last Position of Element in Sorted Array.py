from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return [self.bisect_left(nums, target, left , mid), self.bisect_right(nums, target, mid, right)]
        return [-1, -1]
    
    def bisect_left(self, nums, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

    def bisect_right(self, nums, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return right

"""
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]
"""

s = Solution()

s.searchRange([5,7,7,8,8,10], 8)
s.searchRange([5,7,7,8,8,10], 6)
s.searchRange([],0)