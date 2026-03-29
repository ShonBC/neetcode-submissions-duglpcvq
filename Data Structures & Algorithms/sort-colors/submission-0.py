class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1
        i = 0
        for c in range(len(counts)):
            for j in range(counts[c]):
                nums[i] = c
                i += 1
            
