class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n) n = len(nums)
        Space Complexity: O(1)
        """
        slow = 0
        fast = 0
        while True:
            # Find cycle
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            # Find duplicate
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
            
