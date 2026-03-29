class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Time Complexity: O(n) n = len(height)
        Space Complexity: O(1)
        '''
        if len(height) == 0:
            return 0
        L, R, area = 0, len(height) - 1, 0
        maxL, maxR = height[L], height[R]
        while L < R:
            if maxL < maxR:
                L += 1
                maxL = max(maxL, height[L])
                area += maxL - height[L]
            else:
                R -= 1
                maxR = max(maxR, height[R])
                area += maxR - height[R]
        return area