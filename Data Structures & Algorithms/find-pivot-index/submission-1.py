class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len(nums)
        Space Complexity: O(1)
        '''
        total = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            rsum = total - nums[i] - lsum
            if lsum == rsum:
                return i
            lsum += nums[i]
        return -1