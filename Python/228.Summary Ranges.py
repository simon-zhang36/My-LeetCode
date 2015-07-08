class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        nums.sort()
        nums.append(None)
        a = str(nums[0])
        b = ""
        ranges = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                b = str(nums[i])
            else:
                if b == "":
                    ranges.append(a)
                else:
                    ranges.append(a + "->" + b)
                a = str(nums[i])
                b = ""
        return ranges


class Solution2:
        # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]