class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len of nums
        Space Complexity: O(n) n = size of nums array
        '''
        total = {0: nums[0]}
        ans = nums[0]
        for i in range(1, len(nums)):
            total[i] = max(total[i - 1], nums[i] + total.get(i - 2, 0)) # Take into account skipping a house to maximize profits.
            ans = max(ans, total[i])
        
        return ans