class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        seen = {}
        for val in nums:
            if val not in seen:
                seen[val] = 1
            else:
                seen[val] += 1
        ans = []
        for key, val in seen.items():
            if val > len(nums) / 3:
                ans.append(key)
        return ans