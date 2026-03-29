class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Time Complexity: O(n) n = len(nums)
        Space Complexity: O(m) m = # distinct totals, O(n) in worst case
        '''
        pre = {0 : 1}
        ans = total = 0
        for n in nums:
            total += n
            dif = total - k
            ans +=  pre.get(dif, 0)

            pre[total] = pre.get(total, 0) + 1

        return ans        
        