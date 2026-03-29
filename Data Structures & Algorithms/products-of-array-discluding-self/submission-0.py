class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [] # product of elements before each index
        post = [] # product of elements after each index
        ans = []
        total = 1
        for val in nums:
            pre.append(total)
            total = total * val
        total = 1
        for val in reversed(nums):
            post.insert(0, total)
            total = total * val
        
        for i in range(len(nums)):
            ans.append(pre[i] * post[i])
        return ans