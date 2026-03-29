class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = 0
        while r < len(nums):
            if val != nums[r]:
                nums[l] = nums[r]
                l += 1
            r += 1
        return l