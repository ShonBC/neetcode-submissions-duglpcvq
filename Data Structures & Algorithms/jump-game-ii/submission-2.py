class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            mdist = max(l + nums[l], r + nums[r])
            l = r + 1
            r = mdist
            jumps += 1
        return jumps