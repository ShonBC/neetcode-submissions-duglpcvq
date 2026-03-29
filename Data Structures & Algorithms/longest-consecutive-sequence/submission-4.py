class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(n) n is len(nums)
        Space Complexity: O(n)
        '''

        num_set = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in num_set:
                temp = 1
                while num + temp in num_set:
                    temp += 1
                ans = max(ans, temp)
        return ans