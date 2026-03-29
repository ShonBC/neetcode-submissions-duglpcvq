class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        Kadanes Algorithm with a seen set to catch a loop
        '''
        curMax, curMin = 0, 0
        totalMax, totalMin = nums[0], nums[0]
        total = 0
        for n in nums:
            total += n
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            totalMax = max(totalMax, curMax)
            totalMin = min(totalMin, curMin)
        print(totalMin, total, totalMax)
        return max(total - totalMin, totalMax) if totalMax > 0 else totalMax

