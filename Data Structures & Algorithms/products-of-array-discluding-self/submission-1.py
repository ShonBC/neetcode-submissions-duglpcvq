class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1]
        ans = []
        l = len(nums)
        for i in range(1, l):
            pre.append(pre[i-1] * nums[i-1])
            post.append(post[i-1] * nums[l-i])
        post.reverse()
        for i in range(len(nums)):
            ans.append(pre[i] * post[i])
        return ans