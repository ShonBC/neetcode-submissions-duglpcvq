class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len(heights)
        Space Complexity: O(1)
        '''
        L, R, volume = 0, len(heights) - 1, 0
        while L < R:
            volume = max(volume, (R - L) * min(heights[L], heights[R]))
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1
        return volume