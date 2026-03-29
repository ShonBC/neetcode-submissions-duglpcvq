class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''Kadanes Algorithm
        Time Complexity: O(n)
        Space Complexity: O(n)
        '''
        mSum = nums[0]
        cur = 0
        for n in nums:
            cur = max(cur, 0) + n
            mSum = max(mSum, cur)
        return mSum