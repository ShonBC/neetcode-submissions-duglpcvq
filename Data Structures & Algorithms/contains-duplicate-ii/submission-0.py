class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Time Complexity: O(n) n = len(nums)
        Space Complexity: O(min(n, k)) window will be of size min(len(nums), k)
        '''

        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False