class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jd = 0
        idx = 0
        for num in nums:
            jd = max(jd, num)
            if jd < 1:
                return idx == len(nums) - 1
            jd -= 1
            idx += 1
        return True