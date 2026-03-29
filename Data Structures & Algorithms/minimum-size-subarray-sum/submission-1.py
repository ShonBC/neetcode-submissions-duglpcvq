class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len(nums)
        Space Complexity: O(1)
        '''
        length = float('inf')
        L = 0
        total = 0
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(R - L + 1, length)
                total -= nums[L]
                L += 1
        return length if length != float('inf') else 0