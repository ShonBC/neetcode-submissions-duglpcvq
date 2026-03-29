class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        for val in nums:
            if val == ans:
                count += 1
            else:
                count -= 1
                if count <= 0:
                    ans = val
                    count = 1
        return ans