class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        if mid < right: shift right over
        else shift left over to mid + 1
        repeate until left == right or left = right - 1
        return nums[left]
        Time Complexity: O(log(n)) n is len(nums)
        Space Complexity: O(1)
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]