class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n*(1+n) // 2 - sum(nums)