from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:
                if nums[mid] >= target >= nums[0]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[-1]:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid
        if nums[left] < target or nums[left] > target:
            return -1
        
        return left


s = Solution()

s.search([1],1)
s.search([1,2,3,1],4)
s.search([4,5,6,7,0,1,2],0)
s.search([4,5,6,7,0,1,2],3)
# s.search([3,2,1])
# s.search([1,2,3])

