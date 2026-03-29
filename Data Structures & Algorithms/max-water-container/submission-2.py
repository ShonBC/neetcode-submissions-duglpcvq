class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len(heights)
        Space Complexity: O(1)
        '''
        l = 0
        r = len(heights) - 1
        vol = 0
        while l < r:
            cur = (r - l) * min(heights[l], heights[r])
            vol = max(vol, cur)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return vol