def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(nums, choosen) -> None:
        if not nums:
            res.append(choosen)
        else:
            dfs(nums[1:], choosen + [nums[0]])
            dfs(nums[1:], choosen)

    dfs(nums, [])

    return res