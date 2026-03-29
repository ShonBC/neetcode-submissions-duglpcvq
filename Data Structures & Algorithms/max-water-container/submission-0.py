class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len(heights)
        Space Complexity: O(1)
        '''
        ans = 0 # max(ans, area)
        L, R = 0, len(heights) - 1
        while L < R:
            area = (R - L) * (min(heights[L], heights[R]))
            ans = max(ans, area)
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return ans