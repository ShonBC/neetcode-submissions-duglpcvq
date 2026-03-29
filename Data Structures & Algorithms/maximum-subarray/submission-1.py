class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = 0
        for i in nums:
            cur = max(cur, 0) + i
            ans = max(ans, cur)
        return ans