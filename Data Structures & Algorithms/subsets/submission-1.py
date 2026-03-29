class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for num in nums:
            res += [sub + [num] for sub in res]
        return res