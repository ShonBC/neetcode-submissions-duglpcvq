class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = 0
        right = 1
        ans = 0
        nums.sort() # O(log(n))
        while right <= len(nums) - 1: # O(n)
            if nums[right] == nums[right - 1]:
                left += 1
                right += 1
                continue
            if nums[right] != nums[right - 1] + 1:
                ans = max(ans, right - left)
                left = right
            right += 1
        return max(ans, right - left)